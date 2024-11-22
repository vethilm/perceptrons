import numpy as np
import random

class Perceptron:
    def __init__(self, x, y):
        self.x=x
        #insert bias neuron at beginning of input array
        self.x.insert(0,0)
        self.y=y
        self.w = []
        self.epochs = 0
        #initialize weights as random numbers -0.5 - .0.5
        for i in range(len(x)):
            self.w.append(random.randrange(-5,5)/10 )
        self.alpha = 0.1

    #calculates the weighted sum of inputs
    def weighted_sum(self):
        sum = 0
        for i in range(len(self.x)) :
            sum+= self.x[i]*self.w[i]
        #sum -= self.x[0]*self.w[0]
       # sum = round(sum,1)
        return sum
    
    # activation function 
    def step(self):
        return 1 if self.weighted_sum() > 0 else -1 

    # training method - changes weights until output is correct
    def predict(self):
        while True:
            e = self.alpha * (self.y - self.step())
            if (e == 0):
                return self.w
            if(self.epochs >= 100):
                return self.w
            for i in range(len(self.x)):
                self.epochs+=1
                self.w[i] = round(self.w[i] + (e * self.x[i]),2)
    
    # test perceptron by getting output from trained weights 
    def test(self, weights):
        self.w = weights
        output = self.step()
        return output

