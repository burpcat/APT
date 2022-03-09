# https://www.codechef.com/problems/PCJ18B

def checker(n):
    
    count=0
    for i in range(1,n+1,2): #step size is 2
        
        side_c = n-i+1
        count += (side_c * side_c)
    
    return count


basic_input = int(input())

for _ in range(basic_input):
    n = int(input())
    print(checker(n))


# take a pen and paper, and implement the problem first, then search for patterns
# formula for odd squares horizontally is ((total sides)-(current odd threshold)+1)
# the above formula must be done for vertical also