import gym
from stable_baselines3 import PPO
from custom_env.rubix_env import RubixEnv

models_dir = "models/1664937107"

env = RubixEnv()
env.reset(10, True)

model_path = f"{models_dir}/4500000"
model = PPO.load(model_path, env=env)

episodes = 5

rewards = 0
for ep in range(episodes):
    obs = env.reset(10, True)
    done = False
    print(rewards)
    while not done:
        action, _states = model.predict(obs, deterministic=True)
        obs, rewards, done, info = env.step(action)