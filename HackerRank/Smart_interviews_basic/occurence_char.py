# https://www.hackerrank.com/contests/smart-interviews-basic/challenges/si-basic-occurrence-of-a-character-1
# Smart Interviews Basic > Occurrence of a character

basic_input = input()
char_input = input()
count = 0

for elem in basic_input:
    if char_input == elem :
        count = count + 1


print(count)