# https://www.hackerrank.com/contests/smart-interviews-basic/challenges/si-basic-right-angled-triangle-pattern-1
# Smart Interviews Basic > Right-angled Pattern 1

basic_input = input()
n=0
num = 1

while(n<int(basic_input)):               # to limit the number of times a number is printed (num ) variable
    for i in range(0,int(basic_input)):
        for j in range(0,i+1):
            print(f'{num} ', end= '')
            num = num+1
        n= n+1
        print()
