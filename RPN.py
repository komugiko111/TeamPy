# -*- coding: utf-8 -*-
"""
Created on Thu Oct  8 16:14:59 2020

@author: masaki
"""

def RPN (formula):
    def calc(x,y,z):
        if z == '+':
            return x + y
        elif z == '-':
            return x - y
        elif z == '*':
            return x * y
        elif z == '/':
            return x / y
        else:
            raise ValueError(str(z) + 'is not operator')

    stack = formula.split(' ')
    print(stack)
    while len(stack) != 1:
        c = 0
        while 1:
            try:
                stack[c] = float(stack[c])
            except ValueError:
                    if stack[c] ==' ':
                        stack.pop(c)
                        break
                    stack[c-2]= calc(stack[c-2],stack.pop(c-1),stack.pop(c-1))
                    print(stack)
                    break
            c+=1  
    
    return stack[0]
     
print(RPN('6 6 * 9 - 2 5 + /'))