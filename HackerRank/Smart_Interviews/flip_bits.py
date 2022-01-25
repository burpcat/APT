# https://www.hackerrank.com/contests/smart-interviews/challenges/si-flip-bits
# Smart Interviews > Flip Bits

basic_input = int(input())

def check_flip_bits(nums):
    
    count = 0
    
    a = nums[0]
    b = nums[1]
    
    result = a ^ b  # using bitwise XOR , we can get the difference in value
    
    bin_result = (bin(result)[2:]) # convert given result variable into binary num and string concatenate it

    for i in bin_result:
        if i == '1':
            count+=1
        
    return count

for i in range(basic_input):
    nums = list(map(int,input().split()))

    print(check_flip_bits(nums))
