import matplotlib.pyplot as plt
import numpy as np

# 2x^4 - 5x^3
funcInput = [{'coef': 2, 'degree': 4}, {'coef': -5, 'degree': 3}]


def devirative(function):
    result = []
    for i in range(len(function)):
        coef = function[i]['coef'] * function[i]['degree']
        degree = function[i]['degree'] - 1
        if degree >= 0:
            result.append({'coef': coef, 'degree': degree})

    return result

def func(x, function):
    result = 0
    for i in range(len(function)):
        result += function[i]['coef'] * (x ** function[i]['degree'])
    return result

def findMin(a, b, funcDevirative):
    if abs(b - a) < 0.0001:
        return (a + b) / 2

    ratio = 0.382
    result = 0

    leftPoint = a + ratio * (b - a)
    rightPoint = b - ratio * (b - a)

    leftY = func(leftPoint, funcDevirative)
    rightY = func(rightPoint, funcDevirative)

    if leftY > 0 and rightY > 0:
        result = findMin(a, leftPoint, funcDevirative)

    if leftY < 0 < rightY:
        result = findMin(leftPoint, rightPoint, funcDevirative)

    if leftY < 0 and rightY < 0:
        result = findMin(rightPoint, b, funcDevirative)
    return result

def graph(X, Y, descr, figureNum):
    plt.figure(figureNum)
    plt.plot(X, Y, label = descr)
    plt.legend()

funcDevirative = devirative(funcInput)

a = -2
b = 3

X = np.arange(a, b + 0.1, 0.1)
Y = []

for i in range(len(X)):
    Y.append(func(X[i], funcInput))

graph(X, Y, '2x^4 + 5x^3', 1)
result = findMin(a, b, funcDevirative)

plt.scatter(result, func(result, funcInput))
plt.show()
print("Минимум", result)
