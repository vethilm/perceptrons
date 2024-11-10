import numpy as np
import random

class Perceptron:
    def __init__(self, x, y):
        self.x=x
        self.y=y
        self.w = []
        #initialize weights as random numbers -0.5 - .0.5
        for i in range(len(x)):
            self.w.append(random.randrange(-5,5)/10 )
        self.alpha = 0.1

    def weighted_sum(self):
        sum = 0
        for i in range(len(self.x)) :
            sum+= self.x[i]*self.w[i]
        #sum -= self.x[0]*self.w[0]
       # sum = round(sum,1)
        return sum
    
    def step(self):
        return 1 if self.weighted_sum() > 0 else -1 

    def predict(self):
        while True:
            e = self.alpha * (self.y - self.step())
            print(self.y, "-", self.step(), "=",e)
            if (e == 0):
                print("output acheived")
                return self.w
            for i in range(len(self.x)):
                self.w[i] = round(self.w[i] + (e * self.x[i]),2)
    def test(self, weights):
        self.w = weights
        output = self.step()
        return output

