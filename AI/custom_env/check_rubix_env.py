from stable_baselines3.common.env_checker import check_env
from rubix_env import RubixEnv

env = RubixEnv()


check_env(env)
