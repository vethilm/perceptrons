
import Perceptron as P
import json

numInputs = 5
avg_weights = [0,0,0,0,0]
testDataIndex = 0

with open ('data.json','r') as file:
    data = json.load(file)
    for i in range(16):
        index = data['inputs'][i][2]
        x  = data['inputs'][i][0]
        #insert bias neuron at beginning of x array
        x.insert(0,1)
        #get desired output from data
        y  = data['inputs'][i][1]
        print(x,y)
        if(index == testDataIndex):
            test = P.Perceptron(x,y)
        else:
            #create perceptron object with inputs and desired output
            p = P.Perceptron(x,y)
            #get the weights from the perceptron
            final_weights = p.predict()
            print("f",final_weights)
            for w in range(5):
                avg_weights[w] += final_weights[w]
#get average weights
for i in range(numInputs):
    avg_weights[i] = avg_weights[i]/numInputs

print(test.test(avg_weights))

