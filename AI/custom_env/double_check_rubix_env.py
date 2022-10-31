from rubix_env import RubixEnv


env = RubixEnv()
episodes = 2

for episode in range(episodes):
	obs = env.reset(1)
	for step in range(10):
		random_action = env.action_space.sample()
		print("action",random_action)
		obs, reward, done, info = env.step(random_action)
		print('reward',reward)