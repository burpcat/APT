#https://www.codechef.com/FEB221C/problems/EUREKA
# Solution : 57754779

from math import floor

basic_input = int(input())

def n_queen(n):
    formula = ((0.143*n)**n)

    if((formula-floor(formula))<0.5):
        print(floor(formula))
    else:
        print(floor(formula)+1)

for i in range(basic_input):
    some_num = int(input())
    n_queen(some_num)