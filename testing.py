from data_env import Env

env = Env()

data, tp = env.getYardData(1, 25, 'Rush')
hist = env.getHistogram(data)
env.plotHistogram(data, hist)
