# https://www.codechef.com/MARCH221C/problems/CHFCLASS

def checker(days):
    
    count = days //7
    extra = days % 7
    if(extra == 6):
        return count+1
    else:
        return count

basic_input = int(input())

for _ in range(basic_input):
    days = int(input())
    print(checker(days))