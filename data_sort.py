import pandas as pd
import scipy.stats
import matplotlib.pyplot as plt
import numpy as np

percentagearr = []

df = pd.read_csv("pbp-2020.csv")

# sorting all of the plays by which section of the field they are in
for i in range(0,10):
    arr = df[df.YardLine.between(0+i*10,10+i*10)]
    percentagearr.append(arr)

# further breaking those plays down into which down
down_matrix = []
for i in range(0,10):
    zone_matrix = []
    for j in range(1,5):
        cur_data = percentagearr[i]
        int_arr = cur_data[cur_data['Down'].isin([j])]
        zone_matrix.append(int_arr)
    down_matrix.append(zone_matrix)



curr = down_matrix[0][0]
passssss= curr[curr['IsPass'].isin([1])]
ruuuuuuun= curr[curr['IsRush'].isin([1])]
yards = passssss["Yards"]
yards2 = ruuuuuuun["Yards"]

hist = np.histogram(yards, bins=100)
hist_dist = scipy.stats.rv_histogram(hist)

X = np.linspace(-8.0, 50.0, 100)
plt.title("PDF from Template")
plt.hist(yards, density=True, bins=100)
plt.plot(X, hist_dist.pdf(X), label='PDF')
plt.plot(X, hist_dist.cdf(X), label='CDF')
plt.show()



print("ppp")
