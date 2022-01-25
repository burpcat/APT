# https://www.hackerrank.com/contests/smart-interviews/challenges/si-check-power-of-two
# Smart Interviews > Check Power of Two

from math import log10,ceil,floor 
# imported these directly, because using . makes program slower in general

basic_input = int(input())

def check_power(num_input):
    if num_input ==0:
        return False
    else:
        return (ceil(log10(num_input)/log10(2))==floor(log10(num_input)/log10(2)))

        #

for i in range(basic_input):
    num_input = int(input())
    print(check_power(num_input))