import random

class Perceptron:
    def __init__(self, x, y, threshold):
        self.x=x
        #insert bias neuron at beginning of input array
        self.x.insert(0,1)
        self.y=y
        self.threshold = threshold
        self.w = []
        self.epochs = 0
        #initialize weights as random numbers -0.5 - .0.5
        for i in range(len(x)):
            self.w.append(random.randrange(-5,5)/10 )
        self.alpha = 0.1
        self.trainingAccuracy = 0  

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
        return 1 if self.weighted_sum() > self.threshold else -1 

    # training method - changes weights until output is correct
    def train(self):
        while True:
            output = self.step()
            error = 0 if self.y == output else 1
            #print(self.y, output, error)
            if (error == 0):
                self.trainingAccuracy+=1
                return self.w
            if(self.epochs >= 10000):
                return self.w
            for i in range(len(self.x)):
                self.epochs+=1
                delta = self.alpha *(self.y - output)*self.x[i]
                self.w[i] = round(self.w[i] + (delta ),2)
    
    # test perceptron by getting output from trained weights 
    def test(self, weights):
        self.w = weights
        output = self.step()
        return output

