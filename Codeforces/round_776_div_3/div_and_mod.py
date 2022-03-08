# https://codeforces.com/contest/1650/problem/B

def checker(l,r,a):
    # max = 0
    # for x in range(l,r+1):
    #     form = ((x//a)+(x%a))
    #     if ((form)>max):
    #         max = form
    
    # return form
    if (r == a):
       return a-1
    elif (r%a ==0):
        return (((r-1)//a)+((r-1)%a))
    else:
        return ((r//a)+(r%a))

basic_input = int(input())

for i in range(basic_input):
    some_list = list(map(int,input().split()))

    print(checker(some_list[0],some_list[1],some_list[2]))
    
