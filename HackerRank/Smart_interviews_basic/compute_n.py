# https://www.hackerrank.com/contests/smart-interviews-basic/challenges/si-basic-compute-n
# Smart interviews basic > Compute N!

basic_input = input()
prod = 1

for i in range(1,int(basic_input)+1):
    prod = prod * i

print(prod)