import Perceptron as P
import random

# generates x random test sample pairs
# input being the cmyk values and output being 1 if the color is over saturated and 0 otherwise
def generateData(x):
    data=[]
    for i in range(x):
        cmyk = [0,0,0,0]
        sum = 0
        for j in range(len(cmyk)):
            cmyk[j] = random.randrange(0,100)
            sum+= cmyk[j]
        data.append([cmyk, 1 if sum < 240 else -1])
    return data
        
def train(n):
    numInputs = 5
    trainingData = generateData(n)
    avg_weights = [0,0,0,0,0]
    trainingAccuracy=0
    for sample in trainingData:
        p = P.Perceptron(sample[0],sample[1],240)
        final_weights = p.train()
        trainingAccuracy+= p.trainingAccuracy
        for w in range(5):
            avg_weights[w] += final_weights[w]
    #get average weights
    for i in range(numInputs):
        avg_weights[i] = round(avg_weights[i]/numInputs,4)
    return avg_weights, trainingAccuracy

trainingSamples = 1000
trained_weights, trainingAccuracy = train(trainingSamples)
print("Training Accuracy:",trainingAccuracy,"/",trainingSamples)

def test(n,w):
    testData =generateData(n)
    totalError = 0
    for sample in testData:
        p = P.Perceptron(sample[0],sample[1],240)
        # get output from testing with the trained weights
        testOutput = p.test(w)
        # calculate test error
        testError = 1 if p.y == testOutput else -1
        # calculate error
        totalError += testError
    print("Test Accuracy: ",n-totalError,"/",n, "=",round((n-totalError)/n,2))
         

test(400,trained_weights)


