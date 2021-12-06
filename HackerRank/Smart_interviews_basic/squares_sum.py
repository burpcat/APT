# https://www.hackerrank.com/contests/smart-interviews-basic/challenges/si-basic-squares-sum
# Smart Interviews Basic > Squares sum

basic_input = input()
sum =0

for i in range(int(basic_input)+1):
    sum = sum + (i*i)

print(sum)