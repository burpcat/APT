# https://www.hackerrank.com/contests/smart-interviews-basic/challenges/si-basic-odd-even-index
# Smart Interviews Basic > Odd Even Index

basic_input = input()
i = 1
str_even = str_odd = ''

for elem in basic_input:
    if(i%2) == 0:
        str_even = str_even + elem   
    else:
        str_odd = str_odd + elem
    i=i+1

print(str_even+str_odd)