# https://www.hackerrank.com/contests/smart-interviews-basic/challenges/si-basic-triangle-validator
# Smart Interviews Basic > Triangle Validator

basic_input = input()
basic_list = list(map(int,basic_input.split())) # converting a string to a number array

if ((basic_list[0]+basic_list[1])> basic_list[2]):
    if ((basic_list[1]+basic_list[2])> basic_list[0]):
        if ((basic_list[0]+basic_list[2])> basic_list[1]):
            print('Yes')
        else:
            print('No')
    else:
        print('No')
else:
    print('No')