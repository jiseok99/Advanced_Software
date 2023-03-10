import numpy as np
import pytest

import gym
from gym.vector.sync_vector_env import SyncVectorEnv
from tests.vector.utils import make_env

ENV_ID = "CartPole-v1"
NUM_ENVS = 3
ENV_STEPS = 50
SEED = 42


@pytest.mark.parametrize("asynchronous", [True, False])
def test_vector_env_info(asynchronous):
    env = gym.vector.make(
        ENV_ID, num_envs=NUM_ENVS, asynchronous=asynchronous, disable_env_checker=True
    )
    env.reset(seed=SEED)
    for _ in range(ENV_STEPS):
        env.action_space.seed(SEED)
        action = env.action_space.sample()
        _, _, dones, infos = env.step(action)
        if any(dones):
            assert len(infos["terminal_observation"]) == NUM_ENVS
            assert len(infos["_terminal_observation"]) == NUM_ENVS

            assert isinstance(infos["terminal_observation"], np.ndarray)
            assert isinstance(infos["_terminal_observation"], np.ndarray)

            for i, done in enumerate(dones):
                if done:
                    assert infos["_terminal_observation"][i]
                else:
                    assert not infos["_terminal_observation"][i]
                    assert infos["terminal_observation"][i] is None


@pytest.mark.parametrize("concurrent_ends", [1, 2, 3])
def test_vector_env_info_concurrent_termination(concurrent_ends):
    # envs that need to terminate together will have the same action
    actions = [0] * concurrent_ends + [1] * (NUM_ENVS - concurrent_ends)
    envs = [make_env(ENV_ID, SEED) for _ in range(NUM_ENVS)]
    envs = SyncVectorEnv(envs)

    for _ in range(ENV_STEPS):
        _, _, dones, infos = envs.step(actions)
        if any(dones):
            for i, done in enumerate(dones):
                if i < concurrent_ends:
                    assert done
                    assert infos["_terminal_observation"][i]
                else:
                    assert not infos["_terminal_observation"][i]
                    assert infos["terminal_observation"][i] is None
            return
