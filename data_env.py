import pandas as pd
import scipy.stats
import matplotlib.pyplot as plt
import numpy as np


class data_env:
    def __init__(self):

        YEARS = [2019, 2018, 2017]

        data = pd.DataFrame()

        for i in YEARS:
            # low_memory=False eliminates a warning
            i_data = pd.read_csv('https://github.com/nflverse/nflfastR-data/blob/master/data/' \
                                 'play_by_play_' + str(i) + '.csv.gz?raw=True',
                                 compression='gzip', low_memory=False)

            # sort=True eliminates a warning and alphabetically sorts columns
            data = data.append(i_data, sort=True)
        percentagearr = []
        # Give each row a unique index
        data.reset_index(drop=True, inplace=True)
        df = data
        # sorting all of the plays by which section of the field they are in
        for i in range(0, 10):
            arr = df[df.yardline_100.between(0+i*10, 10+i*10)]
            percentagearr.append(arr)

        # further breaking those plays down into which down
        down_matrix = []
        for i in range(0, 10):
            zone_matrix = []
            for j in range(1, 5):
                cur_data = percentagearr[i]
                int_arr = cur_data[cur_data['down'].isin([j])]
                zone_matrix.append(int_arr)
            down_matrix.append(zone_matrix)
        self.down_matrix = down_matrix

    def getYardData(self, down, yardmark, playType):
        yard_mark = int(yardmark//10)
        curr = self.down_matrix[yard_mark][down-1]

        if playType == "Pass":
            data = curr[curr['play_type'].str.contains('pass', na=False)]
            yards = data['yards_gained']
        elif playType == 'Rush':
            data = curr[curr['play_type'].str.contains('run', na=False)]
            yards = data['yards_gained']
        elif playType == "Punt":
            data = curr[curr['play_type'].str.contains('punt')]
            yards = data['kick_distance']
            yards = yards.dropna()
        return yards

    def getHistogram(self, yardData):
        hist = np.histogram(yardData, bins=110)
        hist_dist = scipy.stats.rv_histogram(hist)
        return hist_dist

    def plotHistogram(self, yardData, hist_dist):
        X = np.linspace(-10.0, 50.0, 60)
        plt.title("PDF from Template")
        plt.hist(yardData, density=True, bins=110)
        plt.plot(X, hist_dist.pdf(X), label='PDF')
        #plt.plot(X, hist_dist.cdf(X), label='CDF')

        plt.show()




