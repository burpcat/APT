# https://www.hackerrank.com/contests/smart-interviews-basic/challenges/si-basic-number-reverse
# Smart Interviews Basic > Number Reverse

basic_input = input()
main_str = ''

for i in range(len(basic_input)):
    last_digit = int(basic_input) %10
    main_str = main_str + str(last_digit)
    basic_input = int(basic_input) //10

print(main_str)