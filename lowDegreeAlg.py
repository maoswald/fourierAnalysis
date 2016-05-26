# -*- coding: utf-8 -*-

import random
import inspect

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

def genExamples(boolean, type=1):
    #Todo: Number of Examples
    n = 5
    examples = []                                       # 0 - 1
    examplesMath = []                                   # 1 - -1
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

    coefficients = [0,1]                # coefficients +1
    boolean = lambda x,y: x or y        # max function
    #print genExamples(boolean, 1)
    
    print lowDegree(genExamples(boolean), coefficients)


