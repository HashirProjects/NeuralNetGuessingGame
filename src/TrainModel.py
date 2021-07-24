import numpy as np
from tensorflow import keras
import os
from src.LoadData import load, InsufficientDataError


class TrainModel():

    def __init__(self,userInput):  
        
        if len(userInput) < 100:
            raise InsufficientDataError("Too little data for NN to provide accurate predictions, Please provide more than 100 entries")
            return

        self.x, self.y =load(userInput)

    def Train(self):
        
        model = keras.Sequential()
        
        model.add(keras.layers.Input(shape=(10,)))
        model.add(keras.layers.Dense(units=100, activation='relu' ))
        model.add(keras.layers.Dropout(0.2))
        model.add(keras.layers.Dense(units=50, activation='relu' ))
        model.add(keras.layers.Dropout(0.2))
        model.add(keras.layers.Dense(units=10, activation='softmax')) # 10 nodes for the ten different digits possible

    
        initial_learning_rate = 0.01
        lr_schedule = keras.optimizers.schedules.ExponentialDecay(
            initial_learning_rate,
            decay_steps=100000,
            decay_rate=0.96,
            staircase=True)
        
        model.compile(optimizer=keras.optimizers.SGD(learning_rate=lr_schedule), loss='categorical_crossentropy', metrics=[keras.metrics.CategoricalAccuracy()])#i wrote a pretty large model  since the task is relatively complex

        history = model.fit(self.x, self.y, epochs=20)# you have to experiement and see if more epochs are reducing the loss more
        model.save('C:/Users/hashi/OneDrive/Desktop/Programming/NN_GuessingGame/src/UserModel')