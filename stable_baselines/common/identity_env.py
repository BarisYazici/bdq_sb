import numpy as np

from gym import Env
from gym.spaces import Discrete, MultiDiscrete, MultiBinary


class IdentityEnv(Env):
    def __init__(self, dim, ep_length=100):
        """
        Identity environment for testing purposes

        :param dim: (int) the size of the dimensions you want to learn
        :param ep_length: (int) the length of each episodes in timesteps
        """
        self.action_space = Discrete(dim)
        self.observation_space = self.action_space
        self.ep_length = ep_length
        self.current_step = 0
        self.dim = dim

    def reset(self):
        self.current_step = 0
        self._choose_next_state()
        return self.state

    def step(self, action):
        reward = self._get_reward(action)
        self._choose_next_state()
        self.current_step += 1
        done = self.current_step >= self.ep_length
        return self.state, reward, done, {}

    def _choose_next_state(self):
        self.state = self.action_space.sample()

    def _get_reward(self, action):
        return 1 if np.all(self.state == action) else 0

    def render(self, mode='human'):
        pass


class IdentityEnvMultiDiscrete(IdentityEnv):
    def __init__(self, dim, ep_length=100):
        """
        Identity environment for testing purposes

        :param dim: (int) the size of the dimensions you want to learn
        :param ep_length: (int) the length of each episodes in timesteps
        """
        super(IdentityEnvMultiDiscrete, self).__init__(dim, ep_length)
        self.action_space = MultiDiscrete([dim, dim])
        self.observation_space = self.action_space


class IdentityEnvMultiBinary(IdentityEnv):
    def __init__(self, dim, ep_length=100):
        """
        Identity environment for testing purposes

        :param dim: (int) the size of the dimensions you want to learn
        :param ep_length: (int) the length of each episodes in timesteps
        """
        super(IdentityEnvMultiBinary, self).__init__(dim, ep_length)
        self.action_space = MultiBinary(dim)
        self.observation_space = self.action_space
