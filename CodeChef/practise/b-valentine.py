basic_input = int(input())

for _ in range(basic_input):
    len_str = int(input())  # len of the lists
    list_A = list(map(int, input().split()))
    list_B = list(map(int, input().split())) 

    list_A.sort()
    list_B.sort()
    list_B.reverse() # to find the minimum likeness value

    likeness = 0

    for i in range(len_str):
        likeness = max(list_A[i] + list_B[i],likeness) # trying to find the maximum value in the minimum most likenesss
    
    print(likeness)

# Executed
# Py3 - 0.16 sec
#PyPy - 0.13 sec