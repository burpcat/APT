# https://www.hackerrank.com/contests/smart-interviews-basic/challenges/si-basic-digits-in-a-string
# Smart Interviews Basic > Digits in a String

basic_input = input()
count = 0
number_list = [1,2,3,4,5,6,7,8,9,0]
for elem in basic_input:
    try:
        elem = int(elem)   
        if elem not  in list(range(0,10)):
            print(elem)
            continue
        else:
            count = count +1
    except ValueError:
        break

if count == len(basic_input):
    print('Yes')
else:
    print('No')


# same as the before program, we use exception (error) handling to fix errors when we are converting individual
# characters of the string into integers.