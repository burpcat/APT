# https://www.hackerrank.com/contests/smart-interviews-basic/challenges/si-basic-cubes-sum
# Smart Interviews Basic > Cubes sum

basic_input = input()
sum =0

for i in range(int(basic_input)+1):
    sum = sum + (i**3)

print(sum)

