from Sports_env import sports
from data_env import data_env
from search import simple_expectation
import matplotlib.pyplot as plt
data = data_env()

x = []
y = []
for fp in range(1, 100):
    thing = simple_expectation(10, data, fp)
    x.append(fp)
    y.append(thing)
plt.plot(x, y, 'bo')
plt.xlabel("Starting Field Position")
plt.ylabel("Value of Position")
plt.show()