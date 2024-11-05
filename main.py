import Perceptron as P
import os

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

clear_console()

# initilize input values, wehre X[0] is the bias
x = [1,-1,1,1,-1]
y = 1
p = P.Perceptron(x,y)

print("Weights: " ,p.w)
p.predict()