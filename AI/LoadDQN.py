import gym
from stable_baselines3 import DQN
from custom_env.rubix_env import RubixEnv

models_dir = "models/DQN21664946283"

env = RubixEnv()
env.reset(1, True)

model_path = f"{models_dir}/10000000"
model = DQN.load(model_path, env=env)

episodes = 10

rewards = 0
for ep in range(episodes):
    obs = env.reset(1, True)
    done = False
    print(rewards)
    while not done:
        action, _states = model.predict(obs, deterministic=True)
        obs, rewards, done, info = env.step(action)