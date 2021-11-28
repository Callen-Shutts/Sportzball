from Sports_env import sports
from data_env import Env
from search import simple_expectation
import matplotlib.pyplot as plt
data = Env()

x = []
y = []
for fp in range(0, 100):
    thing = simple_expectation(100, data, fp)
    x.append(fp)
    y.append(thing)
plt.plot(x, y, 'bo')
plt.xlabel("Starting Field Position")
plt.ylabel("Value of Position")
plt.show()

