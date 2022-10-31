import gym
from stable_baselines3 import PPO
from custom_env.rubix_env import RubixEnv

models_dir = "models/1665499200"

env = RubixEnv()
env.reset(1, True)

model_path = f"{models_dir}/10000000"
model = PPO.load(model_path, env=env)

episodes = 50

correct = 0
corect_perc = []
rewards = 0
for i in range(15):
    for ep in range(episodes):
        obs = env.reset(1, False)
        done = False
        if rewards == 100:
            correct +=1
        while not done:
            action, _states = model.predict(obs, deterministic=True)
            obs, rewards, done, info = env.step(action)
        print(f" Percent corrcect{correct/episodes*100}%")
    correct_perc.append(correct/episodes*100)

print("average correct: ", sum(correct_perc)/len(correct_perc))
