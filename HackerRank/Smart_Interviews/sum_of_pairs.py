# https://www.hackerrank.com/contests/smart-interviews/challenges/si-sum-of-pairs/problem
# Smart Interviews > Sum of Pairs

# This problem is solved using two pointer method

basic_input = int(input())

def pairs_check(basic_list,len_of_ar,sum):

    i =0                # pin at start
    j= len_of_ar-1      # pin at end (use len-1 since index starts at zero)
    basic_list.sort()

    while(i < j):
       
        if (basic_list[i] + basic_list[j] == sum):
            return True
 
        elif(basic_list[i] + basic_list[j] < sum):  # If start pin and end pin sums are less than sum, then we require more sum
            i += 1                                  # so, we increment the start pin
 
        else:                                       # If the sum is more than required, we decrement the end pin
            j -= 1                                  # this, matches the two points where sum is equal to zero
    return False
    

for i in range(basic_input):
    
    node_list = list(map(int,input().split()))
    basic_list = list(map(int,input().split()))

    print(pairs_check(basic_list,node_list[0],node_list[1]))