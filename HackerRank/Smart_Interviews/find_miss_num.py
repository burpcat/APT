# https://www.hackerrank.com/contests/smart-interviews/challenges/si-finding-missing-number
# Smart Interviews > Finding Missing Number

basic_input = int(input())

def check_func(basic_list,basic_sum):
    original_sum = sum(basic_list)
    return int((basic_sum-original_sum))   # subtract the sum of passed series , so we can get the original missing number

for i in range(basic_input):
    list_len = int(input())+1
    basic_sum = (list_len*(list_len+1))/2 # calculate the original sum of the series (n*(n=1))/2
    basic_list = list(map(int,input().split())) # convert string to list

    print(check_func(basic_list, basic_sum))
