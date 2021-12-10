# https://www.hackerrank.com/contests/smart-interviews-basic/challenges/si-basic-print-half-diamond-pattern
# Smart Interviews Basic > Print half diamond pattern

basic_input = int(input())

for i in range(basic_input):
    for j in range(0,i+1):
        print('*', end="")

    print()

for i in range(basic_input,0,-1):
    for j in range(0,i-1):
        print('*',end="")

    print()