# https://www.hackerrank.com/contests/smart-interviews-basic/challenges/si-basic-narcissistic-numbers
# Smart Interviews Basic > Narcissistic numbers


basic_input = input()
number= int(basic_input)

main_sum =0

for i in range(len(basic_input)):
    last_digit = number%10
    main_sum = main_sum + (last_digit**len(basic_input))
    number = int(number) // 10

if int(basic_input) == main_sum :
    print('Yes')
else:
    print('No')
