
from Sports_env import sports
from data_env import data_env
from stable_baselines3 import PPO





data = data_env()
env = sports(data)

model = PPO("MlpPolicy", env, verbose=1)
model.learn(total_timesteps=1000)

obs = env.reset()
for i in range(1000):
    action, _states = model.predict(obs, deterministic=True)
    obs, reward, done, info = env.step(action)
    if done:
      obs = env.reset()
