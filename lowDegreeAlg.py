# -*- coding: utf-8 -*-

import random
import inspect

def lowDegree(examples, fourierCoefficients):
    return True


def genExamples(boolean):
    n = 5
    examples = []
    args = len(inspect.getargspec(boolean).args)
    randomArgs = []
    for i in range(n):
        for h in range(args):
            #randomArgs.append(-1 if random.randint(0, 1) == 1 else 1)
            randomArgs.append(random.randint(0, 1))
        examples.append((randomArgs, booleanFunction(boolean, randomArgs)))
        randomArgs = []
    return examples

def booleanFunction(function, args):
    return function(*args)



#1. x, f(X) generien
#2. annähern

if __name__ == '__main__':

    boolean = lambda x,y,c: x or y or c  #max
    print genExamples(boolean)

