# https://www.hackerrank.com/contests/smart-interviews-basic/challenges/si-basic-compute-a-power-b
# Compute A power B

basic_input = input()
basic_list = basic_input.split()
multiple = 1


for i in range(int(basic_list[1])):
    multiple = multiple * int(basic_list[0])

print(multiple)
