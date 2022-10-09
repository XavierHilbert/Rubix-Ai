from stable_baselines3 import  DDPG, DQN, SAC, TD3, HerReplayBuffer
from stable_baselines3.common.noise import NormalActionNoise

from custom_env.GoalEnv import RubixEnv
import time
import os

models_dir = f"models/DQNHER{int(time.time())}/"
logdir = f"logs/DQNHER{int(time.time())}/"

if not os.path.exists(models_dir):
    os.makedirs(models_dir)

if not os.path.exists(logdir):
    os.makedirs(logdir)

env = RubixEnv()
env.reset(0)

model = DQN('MlpPolicy', env, 
replay_buffer_class=HerReplayBuffer,
    replay_buffer_kwargs=dict(
      goal_selection_strategy="future",
      # IMPORTANT: because the env is not wrapped with a TimeLimit wrapper
      # we have to manually specify the max number of steps per episode
      max_episode_length=100,
      online_sampling=True,
    ),verbose=1, tensorboard_log=logdir)

TIMESTEPS = 10000
iters = 0
while True:
    iters += 1
    model.learn(total_timesteps=TIMESTEPS, reset_num_timesteps=False, tb_log_name=f"DQNHER")
    model.save(f"{models_dir}/{TIMESTEPS*iters}")
    print("resetting env")
    env.reset(iters)