# https://www.hackerrank.com/contests/smart-interviews/challenges/si-binary-representation/problem
# Smart Interviews > Binaru Representation

# This only works in python, in other langs use manual method of conversion using a while loop
basic_input = int(input())

def bin_conv(main_num):
    bin_num = bin(main_num)
    return bin_num[2:]

for i in range(basic_input):
    main_num = int(input())
    print(bin_conv(main_num))
