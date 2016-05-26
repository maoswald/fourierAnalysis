# -*- coding: utf-8 -*-

import random
import inspect
import numpy as np

def lowDegree(examples, coefficients):
    m = len(examples)
    n = len(examples[0][0])                         # number of input bits n
    approx = 0
    for example in examples:
        temp = 0
        for coefficient in coefficients:
            temp += example[0][coefficient]
        approx += example[1] * (-1)**temp
    return 2**(-n) * approx

def genExamples(boolean, probability, estimation, type=1):
    n = int(round(np.log10(1/probability) / estimation ** 2))               # O(log(1/probability)/estimation**2
    print "Number of Examples: " + str(n)
    examples = []                                                           # 0 - 1
    examplesMath = []                                                       # 1 - -1
    args = len(inspect.getargspec(boolean).args)
    randomArgs = []
    randomArgsMath = []
    for i in range(n):
        for h in range(args):
            rand = random.randint(0, 1)
            randomArgsMath.append(-1 if rand == 1 else 1)
            randomArgs.append(rand)
        result = booleanFunction(boolean, randomArgs)
        examplesMath.append((randomArgsMath, -1 if result == 1 else 1))
        examples.append((randomArgs, result))
        randomArgsMath = []
        randomArgs = []
    if type == 0:
        return examples
    else:
        return examplesMath

def booleanFunction(function, args):
    return function(*args)

if __name__ == '__main__':

    coefficients = [0,1]                                                                          # coefficients +1
    boolean_max = lambda x, y: x or y                                                               # max function
    boolean_majority = lambda a, b, c: (a and b) or (a and c) or (b and c) or (a and b and c)       # majority function

    examples = genExamples(boolean_max, 0.1, 0.1)
    print examples
    print lowDegree(examples, coefficients)


