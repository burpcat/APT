# https://www.hackerrank.com/contests/smart-interviews-basic/challenges/si-basic-vowels-in-a-string
# Smart Interviews Basic > Vowels in a String

basic_input = input()
count = 0

vowel_list = ['a','e','i','o','u']
for elem in basic_input:
    if elem not  in vowel_list:
        continue
    else:
        count = count +1

if count == len(basic_input):
    print('Yes')
else:
    print('No')


# The basic logic of this program is that, it updates the count of the number of vowels inside the string
# and if the count of the vowels is same as the length of the string, then the result is printed to be 'Yes'
# otherwise it is printe to be a 'No'