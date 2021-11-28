from Sports_env import sports
import random
import numpy as np


def simple_expectation(playouts, data, fp=25):
    score_list = []
    for i in range(0, playouts):
        env = sports(data, fp=fp)
        done = False
        while not done:
            play = random.randint(0,1)
            state, reward, done = env.step(play)
        score_list.append(reward)
    return np.array(score_list).mean()

