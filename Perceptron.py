import numpy as np
import random

class Perceptron:
    def __init__(self, x, y):
        #initialize weights as random numbers -0.5 - .0.5
        self.x=x
        self.y=y
        self.w = []
        for i in range(5):
            self.w.append(random.randrange(-5,5)/10 )
        self.alpha = 0.1

    def weighted_sum(self):
        sum = 0
        for i in range(4) :
            sum+= self.x[i+1]*self.w[i+1]
        sum -= self.x[0]*self.w[0]
        sum = round(sum,1)
        return sum
    
    def step(self):
        return 0 if self.weighted_sum(self) <=0 else 1

    def predict(self):
        return 

