import numpy as np
<<<<<<< HEAD

from gym import Env
=======
from typing import Optional

from gym import Env, Space
>>>>>>> upstream/master
from gym.spaces import Discrete, MultiDiscrete, MultiBinary, Box


class IdentityEnv(Env):
<<<<<<< HEAD
    def __init__(self, dim=1, ep_length=100):
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
=======
    def __init__(self,
                 dim: Optional[int] = None,
                 space: Optional[Space] = None,
                 ep_length: int = 100):
        """
        Identity environment for testing purposes

        :param dim: the size of the action and observation dimension you want
            to learn. Provide at most one of `dim` and `space`. If both are
            None, then initialization proceeds with `dim=1` and `space=None`.
        :param space: the action and observation space. Provide at most one of
            `dim` and `space`.
        :param ep_length: the length of each episode in timesteps
        """
        if space is None:
            if dim is None:
                dim = 1
            space = Discrete(dim)
        else:
            assert dim is None, "arguments for both 'dim' and 'space' provided: at most one allowed"

        self.action_space = self.observation_space = space
        self.ep_length = ep_length
        self.current_step = 0
        self.num_resets = -1  # Becomes 0 after __init__ exits.
>>>>>>> upstream/master
        self.reset()

    def reset(self):
        self.current_step = 0
<<<<<<< HEAD
=======
        self.num_resets += 1
>>>>>>> upstream/master
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


class IdentityEnvBox(IdentityEnv):
    def __init__(self, low=-1, high=1, eps=0.05, ep_length=100):
        """
        Identity environment for testing purposes

<<<<<<< HEAD
        :param dim: (int) the size of the dimensions you want to learn
        :param low: (float) the lower bound of the box dim
        :param high: (float) the upper bound of the box dim
        :param eps: (float) the epsilon bound for correct value
        :param ep_length: (int) the length of each episodes in timesteps
        """
        super(IdentityEnvBox, self).__init__(1, ep_length)
        self.action_space = Box(low=low, high=high, shape=(1,), dtype=np.float32)
        self.observation_space = self.action_space
        self.eps = eps
        self.reset()

    def reset(self):
        self.current_step = 0
        self._choose_next_state()
        return self.state
=======
        :param low: (float) the lower bound of the box dim
        :param high: (float) the upper bound of the box dim
        :param eps: (float) the epsilon bound for correct value
        :param ep_length: (int) the length of each episode in timesteps
        """
        space = Box(low=low, high=high, shape=(1,), dtype=np.float32)
        super().__init__(ep_length=ep_length, space=space)
        self.eps = eps
>>>>>>> upstream/master

    def step(self, action):
        reward = self._get_reward(action)
        self._choose_next_state()
        self.current_step += 1
        done = self.current_step >= self.ep_length
        return self.state, reward, done, {}

<<<<<<< HEAD
    def _choose_next_state(self):
        self.state = self.observation_space.sample()

=======
>>>>>>> upstream/master
    def _get_reward(self, action):
        return 1 if (self.state - self.eps) <= action <= (self.state + self.eps) else 0


class IdentityEnvMultiDiscrete(IdentityEnv):
<<<<<<< HEAD
    def __init__(self, dim, ep_length=100):
=======
    def __init__(self, dim=1, ep_length=100):
>>>>>>> upstream/master
        """
        Identity environment for testing purposes

        :param dim: (int) the size of the dimensions you want to learn
<<<<<<< HEAD
        :param ep_length: (int) the length of each episodes in timesteps
        """
        super(IdentityEnvMultiDiscrete, self).__init__(dim, ep_length)
        self.action_space = MultiDiscrete([dim, dim])
        self.observation_space = self.action_space
        self.reset()


class IdentityEnvMultiBinary(IdentityEnv):
    def __init__(self, dim, ep_length=100):
=======
        :param ep_length: (int) the length of each episode in timesteps
        """
        space = MultiDiscrete([dim, dim])
        super().__init__(ep_length=ep_length, space=space)


class IdentityEnvMultiBinary(IdentityEnv):
    def __init__(self, dim=1, ep_length=100):
>>>>>>> upstream/master
        """
        Identity environment for testing purposes

        :param dim: (int) the size of the dimensions you want to learn
<<<<<<< HEAD
        :param ep_length: (int) the length of each episodes in timesteps
        """
        super(IdentityEnvMultiBinary, self).__init__(dim, ep_length)
        self.action_space = MultiBinary(dim)
        self.observation_space = self.action_space
        self.reset()
=======
        :param ep_length: (int) the length of each episode in timesteps
        """
        space = MultiBinary(dim)
        super().__init__(ep_length=ep_length, space=space)
>>>>>>> upstream/master
