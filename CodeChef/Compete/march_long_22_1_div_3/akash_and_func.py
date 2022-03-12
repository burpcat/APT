# https://www.codechef.com/MARCH221C/problems/CHFDBT

# Logic
# every even element in the supposed list is considered to be a repeating number
# so for even elements, half of them are distinct
# so for odd elements, half+1 of them are distinct


def checker(number):
    
    if(number%2==0):
        distinct = number/2
    
    else:
        distinct = ((number/2) + 1)
    
    return int(distinct)
    

basic_input = int(input())

for _ in range(basic_input):
    number = int(input())
    print(checker(number))