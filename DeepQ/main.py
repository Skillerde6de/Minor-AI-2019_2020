import gym
import numpy as np 
# from dqn import Agent

gym_env = gym.make('custom_gym:Xplane-v0')
# gym_env.reset()
# gym_env.test_window()
gym_env.test_window2()
# gym_env.test_keystroke()

# lr = 0.001c
# gam = 0.99
# n_games = 1000
# agent = Agent(learning_rate=lr, gamma=gam, epsilon=1.0, p
#     input_dims=gym_env.observation_space.shape, n_actions=gym_env.action_space.n, batch_size=70, file_name='dq_model_1.h5')
# scores = []
# eps_hist = []

# for i in range(n_games):
#     crashed = False
#     score = 0 
#     observation = gym_env.reset()
#     while not crashed:
#         action = agent.choose_action(observation)
#         new_observation, reward, done, info = gym_env.step(action)
#         score = score + reward
#         agent.store_transition(observation, action, reward, new_observation, crashed)
#         observation = new_observation
#         agent.learn()
#     eps_hist.append(agent.epsilon)
#     scores.append(score)
    


