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
        data.append([cmyk, 0 if sum < 250 else 1])
    return data
        
def train():
    numInputs = 5
    numTraining= 100
    numTesting = 100

    trainingData = generateData(numTraining)
    testData =generateData(numTesting)
    avg_weights = [0,0,0,0,0]

    for sample in trainingData:
        print(sample)
        p = P.Perceptron(sample[0],sample[1])
        final_weights = p.predict()
        print("Final Weights:" , final_weights)
        for w in range(5):
            avg_weights[w] += final_weights[w]
        print("Final Weights:" , avg_weights)
    #get average weights
    for i in range(numInputs):
        avg_weights[i] = round(avg_weights[i]/numInputs,4)

train()
print("wtf")