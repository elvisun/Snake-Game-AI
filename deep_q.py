import random
import gym
import numpy as np
from collections import deque
from keras.models import Sequential
from keras.layers import Dense, Activation, Dropout, Flatten, Conv2D, MaxPooling2D
from keras.optimizers import Adam
import matplotlib.pyplot as plt
from keras import backend as K

import game

EPISODES = 500


class DQNAgent:
    def __init__(self, state_size, action_size):
        self.state_size = state_size    #10, 10
        self.action_size = action_size
        self.memory = deque(maxlen=2000)
        self.gamma = 0.95    # discount rate
        self.epsilon = 0.05  # exploration rate
        self.epsilon_min = 0.01
        self.epsilon_decay = 0.99
        self.learning_rate = 0.001
        self.model = self._build_model()

    def _build_model(self):
        # Neural Net for Deep-Q learning Model
        model = Sequential()
        #model.add(Conv2D(256, kernel_size = (2,2), activation='relu', input_shape=(self.state_size.shape[0], self.state_size.shape[1],1), padding="same"))
        #model.add(Conv2D(712, kernel_size = (2,2), activation='relu', padding="same"))
        #model.add(Conv2D(128, kernel_size = (2,2), activation='relu', padding="same"))
        model.add(Dense(2048, input_dim=5, activation='relu'))#self.state_size.shape[0] * self.state_size.shape[1]
        #model.add(Flatten())
        model.add(Dense(1024, activation='relu'))
        model.add(Dropout(0.5))
        model.add(Dense(512, activation='relu'))
        model.add(Dense(256, activation='relu'))
        model.add(Dropout(0.5))
        model.add(Dense(128, activation='relu'))
        model.add(Dense(64, activation='relu'))
        model.add(Dropout(0.5))
        model.add(Dense(32, activation='relu'))
        model.add(Dense(16, activation='relu'))
        model.add(Dropout(0.5))
        model.add(Dense(8, activation='relu'))
        model.add(Dense(4, activation='linear'))
        model.compile(loss='mse',
                      optimizer=Adam(lr=self.learning_rate))
        return model

    def remember(self, state, action, reward, next_state, done):
        self.memory.append((state, action, reward, next_state, done))

    def act(self, state):
        if np.random.rand() <= self.epsilon:
            return random.randrange(self.action_size)
        act_values = self.model.predict(state)
        return np.argmax(act_values[0])  # returns action

    def replay(self, batch_size):
        minibatch = random.sample(self.memory, batch_size)
        for state, action, reward, next_state, done in minibatch:
            target = reward
            if not done:
                #print(self.model.predict(next_state)[0])
                #print(np.amax(self.model.predict(next_state)[0]))
                target = reward + self.gamma * \
                       np.amax(self.model.predict(next_state)[0])
                #print(target)
            target_f = self.model.predict(state)
            #print(target_f)
            #print(target_f[0])
            #print(" ")
            target_f[0][action] = target
            self.model.fit(state, target_f, epochs=1, verbose=0)
        if self.epsilon > self.epsilon_min:
            self.epsilon *= self.epsilon_decay

    def load(self, name):
        self.model.load_weights(name)

    def save(self, name):
        self.model.save_weights(name)


if __name__ == "__main__":
    env = game.Game()
    state_size = env.observation_space
    action_size = env.action_space
    agent = DQNAgent(state_size, action_size)
    agent.load("./snake-cnn-weights.h5")
    done = False
    batch_size = 32
    stepList = []
    scoreList = []
    for e in range(EPISODES):
        state = env.reset()
        #print(state)
        for step in range(500):
            env.render()
            action = agent.act(state)
            next_state, reward, done, score = env.move(action)
            reward = reward
            agent.remember(state, action, reward, next_state, done)
            state = next_state
            if done:
                #print(game.num_to_action(action))
                print("episode: {}/{}, steps: {} score {}, e: {:.2}"
                      .format(e, EPISODES, step, score, agent.epsilon))
                stepList.append(step)
                scoreList.append(score)
                break
        if len(agent.memory) > batch_size:
            agent.replay(batch_size)
        if e % 10 == 0:
            agent.save("./snake-cnn-weights.h5")
    agent.save("./snake-cnn-weights.h5")
    plt.plot(stepList)
    plt.title("num of steps")
    plt.show()