import numpy as np
import random

class Perceptron:
    def __init__(self, x, y):
        #initialize weights as random numbers -0.5 - .0.5
        self.x=x
        self.y=y
        self.w = [-0.5, 0.7, -0.2, 0.1, 0.9]
       # for i in range(5):
        #    self.w.append(random.randrange(-5,5)/10 )
        self.alpha = 0.1

    def weighted_sum(self):
        sum = 0
        for i in range(5) :
            sum+= self.x[i]*self.w[i]
        #sum -= self.x[0]*self.w[0]
       # sum = round(sum,1)
        print("sum: ", sum)
        return sum
    
    def step(self):
        return 1 if self.weighted_sum() > 0 else 0 

    def predict(self):
        while True:
            e = self.y - self.step()
            print(self.y, "- ", self.step(), "=",e)
            if (e == 0):
                return
            for i in range(4):
                self.w[i] = self.w[i] + (e * self.x[i])
            print("updated weights", self.w)
        

