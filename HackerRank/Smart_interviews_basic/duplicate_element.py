# Find duplicate element in array
# https://www.hackerrank.com/contests/smart-interviews-basic/challenges/si-basic-find-duplicate-element-in-array

basicLen = int(input())
basicStr = input()

# Sample Inputs
# basicLen = int(6)
# basicStr = "5 4 10 9 21 10"

basicList = map(int, basicStr.split())
subList = list()

for ele in basicList:
    if ele not in subList:
        subList.append(ele)
    else:
        print(ele)
