# https://www.codechef.com/START24C/problems/BADMINTON

# Approach
    # chef starts with 1 right position
    # shifts to right for even positions
    # so, total points //2 gives right postitions -1

basic_input = int(input())

def right_check(n):
    print(n//2+1)

for i in range(basic_input):
    points = int(input())
    right_check(points)
