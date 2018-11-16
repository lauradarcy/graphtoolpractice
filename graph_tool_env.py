import gym
from gym import spaces
from gym.utils import seeding
import numpy as np
from graph_tool.all import *

class graph_tool_env(gym.Env):
    """
    """
    def __init__(self):
        self.range = 1000  # Randomly selected number is within +/- this value
        self.bounds = 10000

        self.action_space = spaces.Box(low=np.array([-self.bounds]), high=np.array([self.bounds]))
        self.observation_space = spaces.Discrete(4)

        self.number = 0
        self.guess_count = 0
        self.guess_max = 200
        self.observation = 0

        self.seed()
        self.reset()

    def seed(self, seed=None):
        self.np_random, seed = seeding.np_random(seed)
        return [seed]

    def step(self, action):
        assert self.action_space.contains(action)

        if action < self.number:
            self.observation = 1

        elif action == self.number:
            self.observation = 2

        elif action > self.number:
            self.observation = 3

        reward = 0
        done = False

        if (self.number - self.range * 0.01) < action < (self.number + self.range * 0.01):
            reward = 1
            done = True

        self.guess_count += 1
        if self.guess_count >= self.guess_max:
            done = True

        return self.observation, reward, done, {"number": self.number, "guesses": self.guess_count}

    def reset(self):
        self.number = self.np_random.uniform(-self.range, self.range)
        self.guess_count = 0
        self.observation = 0
        return self.observation
        
