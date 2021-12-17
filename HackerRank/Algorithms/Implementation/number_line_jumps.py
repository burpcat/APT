# https://www.hackerrank.com/challenges/three-month-preparation-kit-kangaroo/problem
# Algorithms > Implementation > Number Line Jumps

def kangaroo(x1, v1, x2, v2):
    while True:
        # as per question x2>x1 so v1 needs to be greater than v2
        if v1 == v2:
            return "NO"
        else:
            # x1-x2 will always negative so if v1>v2 return yes
            ratio = (x1-x2)/(v2-v1)
            if ratio>=0 and ratio.is_integer():
                return "YES"
            else:
                return "NO"
            
basic_input = list(map(int, input().split()))

result=kangaroo(basic_input[0],basic_input[1],basic_input[2],basic_input[3])
print(result)