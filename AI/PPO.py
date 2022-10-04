from stable_baselines3 import PPO
import os
from custom_env.rubix_env import RubixEnv
import time

models_dir = f"models/{int(time.time())}/"
logdir = f"logs/{int(time.time())}/"

if not os.path.exists(models_dir):
	os.makedirs(models_dir)

if not os.path.exists(logdir):
	os.makedirs(logdir)

env = RubixEnv()
env.reset(0)

model = PPO('MlpPolicy', env, verbose=1, tensorboard_log=logdir)

TIMESTEPS = 10
iters = 0
while True:
    iters += 1
    model.learn(total_timesteps=TIMESTEPS, reset_num_timesteps=False, tb_log_name=f"PPO")
    model.save(f"{models_dir}/{TIMESTEPS*iters}")
    print("resetting env")
    env.reset(iters)
    