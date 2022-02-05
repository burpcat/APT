
####### Brute Force Logic done by me #########
# basic_input = input()
basic_input = [ 3,  4,  6,  6,  3]
basic_input.sort()
count =0
basic_len = len(basic_input)

while(True):
# for main_iter in range(7):
    for count_iter in range(basic_len-1):
        basic_input[count_iter] = basic_input[count_iter]+1

    # print(basic_input)
    count = count+1
    basic_input.sort()
    result = all(element == basic_input[0] for element in basic_input)
    if(result):
        break
print(count)



##### Optimized solution below which is submitted #####

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
    

