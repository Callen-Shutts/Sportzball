from Sports_env import sports
from data_env import  Env
data = Env()
env = sports(data)

thing = data.getYardData(2, 25.448, 'Rush')


state, reward, done = env.step(0)
print(state, reward)

state, reward, done = env.step(0)
print(state, reward)

state, reward, done = env.step(0)
print(state, reward)

state, reward, done = env.step(0)
print(state, reward)

state, reward, done = env.step(0)
print(state, reward)
