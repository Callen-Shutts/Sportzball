import gym
from gym import spaces
import numpy as np


class sports(gym.Env):
    def __init__(self, data, down=1, fp=25, g_score=0, b_score=0, yards_to_go=10, pos=1):
        super(sports, self).__init__()
        self.down = down
        self.fp = fp
        self.g_score = g_score
        self.b_score = b_score
        self.yards_to_go = yards_to_go
        self.data = data
        self.play_arr = ['Pass', 'Rush', 'Punt']
        self.pos = pos
        self.observation_space =spaces.Box(np.array([0, 0, -100, 0,0,-1]), np.array([4,100,100,100,100,1]))
        self.action_space = spaces.Discrete(2)

    def step(self, action):
        play = self.play_arr[action]
        data = self.data.getYardData(self.down, self.fp, play)
        hist = self.data.getHistogram(data)
        result = hist.rvs()
        self.fp += result

        # first down check
        if self.yards_to_go - result <= 0:
            self.yards_to_go = 10
            self.down = 1
        # check if the ball was turned over on downs
        elif self.down + 1 > 4:
            self.turn_over_on_downs()
        else:
            self.down += 1
            self.yards_to_go -= result

        # adding checking for TD
        reward = 6*self.pos
        done = True
        self.pos = self.pos*-1
        if self.fp > 100:
            self.td()
        else:
            reward = 0
            done = False
            self.pos = self.pos*-1

        return self.state(), reward, done, {}

    def state(self):
        return [self.down, self.fp, self.yards_to_go, self.g_score, self.b_score]
