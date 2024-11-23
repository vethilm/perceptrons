import Perceptron as P
import json

def partition(index):
    numInputs = 5
    avg_weights = [0,0,0,0,0]
    testDataIndex = index
    with open ('data.json','r') as file:
        data = json.load(file)
        for i in range(16):
            index = data['inputs'][i][2]
            x  = data['inputs'][i][0]
            y  = data['inputs'][i][1]
            # if index matches the test index, create perceptron object to use for testing
            if(index == testDataIndex):
                test = P.Perceptron(x,y,1)
            # otherwise  create a training object and train it
            else:
                #create perceptron object with inputs and desired output
                p = P.Perceptron(x,y,1)
                #get the weights from the perceptron
                final_weights = p.train()
                for w in range(numInputs):
                    avg_weights[w] += final_weights[w]
    #get average weights from training
    for i in range(numInputs):
        avg_weights[i] = round(avg_weights[i]/numInputs,4)
    # get output from testing with the trained weights
    testOutput = test.test(avg_weights)
    # calculate test error
    testError = 0 if test.y == testOutput else 1
    print("Partion Error: ",testError)
    return testError

# run tests with partitions + calculate error
totalError = 0
for x in range(16):
    xError = partition(x)
    totalError += xError
print("Accuracy: ",16-totalError,"/",16, "=",round((16-totalError)/16,2))
    


