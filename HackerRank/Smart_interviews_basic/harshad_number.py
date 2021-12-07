# https://www.hackerrank.com/contests/smart-interviews-basic/challenges/si-basic-harshad-number
# Smart Interviews Basic > Harshad numbers

basic_input = input()
number = int(basic_input)

main_sum =0

for i in range(len(basic_input)):
    last_digit = number %10
    main_sum = main_sum + last_digit
    number = number // 10

if (int(basic_input) % main_sum) ==0 :
    print('Yes')
else:
    print('No')