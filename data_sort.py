percentagearr = []
import pandas as pd
import matplotlib.pyplot as pt
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

x = 1