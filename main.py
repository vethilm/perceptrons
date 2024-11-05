import Perceptron as P
import json


# # initilize input values, wehre X[0] is the bias
# x = [1,-1,1,1,-1]
# print(x)
# y = 1
# p = P.Perceptron(x,y)

# print("Weights: " ,p.w)
# p.predict()

with open ('data.json','r') as file:
    data = json.load(file)
    for i in range(2):
        x  = data['inputs'][i][0]
        x.insert(0,1)
        y  = data['inputs'][i][1]
        print(x,y)
        p = P.Perceptron(x,y)
        p.predict()
