import Perceptron as P

# initilize input values, wehre X[0] is the bias
x = [1,0,0,1,1]
y = 1
p = P.Perceptron(x,y)

print("Weights: " ,p.w)

print(p.weighted_sum())