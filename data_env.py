import pandas as pd
import scipy.stats
import matplotlib.pyplot as plt
import numpy as np


class Env:

    def __init__(self):
        percentagearr = []
        #Import data
        df = pd.read_csv("pbp-2020.csv")
        df1 = pd.read_csv("pbp-2019.csv")
        df2 = pd.read_csv("pbp-2018.csv")
        df3 = pd.read_csv("pbp-2017.csv")
        df = df.append(df1)
        df = df.append(df2)
        df = df.append(df3)

        # sorting all of the plays by which section of the field they are in
        for i in range(0,10):
            arr = df[df.YardLine.between(0+i*10, 10+i*10)]
            percentagearr.append(arr)

        # further breaking those plays down into which down
        down_matrix = []
        for i in range(0, 10):
            zone_matrix = []
            for j in range(1, 5):
                cur_data = percentagearr[i]
                int_arr = cur_data[cur_data['Down'].isin([j])]
                zone_matrix.append(int_arr)
            down_matrix.append(zone_matrix)
        self.down_matrix = down_matrix



    def getYardData(self, down, yardmark, playType):
        yard_mark = yardmark//10
        curr = self.down_matrix[yard_mark][down-1]

        if playType == "Pass":
            data = curr[curr['IsPass'].isin([1])]
        else:

            data = curr[curr['IsRush'].isin([1])]
        yards = data["Yards"]
        touchdown_percent = data['IsTouchdown'].mean()
        return yards, touchdown_percent

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




