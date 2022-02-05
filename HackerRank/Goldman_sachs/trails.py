# # def countMoves(numbers,basic_len):
# #     # Write your code here
# #     numbers.sort()
# #     count =0

# #     while(True):
        
# #         result = all(element == numbers[0] for element in numbers)
# #         if(result):
# #             break

# #         for count_iter in range(basic_len-1):
# #             numbers[count_iter] = numbers[count_iter]+1
# #         print(numbers)

# #         count = count+1
# #         numbers.sort()
# #     print(count)


# # if __name__ == '__main__':
    
# #     basic_len = int(input())
# #     basic_list = []
# #     for elem in range(basic_len):
# #         basic_list.append(int(input()))
    
# #     print(basic_list)
    
# #     countMoves(basic_list,basic_len)
    
# def countMoves(numbers,basic_len):
#     # Write your code here
#     min_number = min(numbers)
 
#     main_sum = sum(numbers)

#     print(main_sum - (basic_len * min_number))



# if __name__ == '__main__':
    
#     basic_len = int(input())
#     basic_list = []
#     for elem in range(basic_len):
#         basic_list.append(int(input()))
    
#     countMoves(basic_list,basic_len)
    

# consecutiveDifference = [-2,-1,-2,5]
consecutiveDifference = [1,2]
lowerBound = 3
upperBound = 4
count =0

maxdiff = float('-inf')
mindiff = float('inf')
runningsum = 0
if len(consecutiveDifference) == 0:
    return 0

if upperBound < lowerBound :
    return 0

for diff in consecutiveDifference:
    runningsum+=diff
    if runningsum > maxdiff:
        maxdiff = runningsum

    if runningsum < mindiff:
        mindiff = runningsum

maxvalidupperbound = upperBound + mindiff if upperBound+mindiff < upperBound else upperBound
minvalidlowerbound = lowerBound + maxdiff if lowerBound + maxdiff > lowerBound else lowerBound

if maxvalidupperbound >= minvalidlowerbound:
    return maxvalidupperbound - minvalidlowerbound + 1
else:
    return 0

# while(True):

#     somebound = lowerBound
#     main_list = [lowerBound]
#     for i in range(len(consecutiveDifference)):
#         next_num = somebound - consecutiveDifference[i]
#         main_list.append(next_num)
#         somebound = next_num
#     lowerBound+=1
#     count+=1
    
#     if(max(main_list)>10):
#         break
#     print(main_list)

# print(count)