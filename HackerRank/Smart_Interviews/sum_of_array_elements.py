# https://www.hackerrank.com/contests/smart-interviews/challenges/si-sum-of-array-elements/problem
# Smart Interviews > Sum of Array Elements

test_case = int(input())
sum =0
for ele in range(test_case):
    unrequired = int(input())  # length
    main_array = list(map(int,input().split()))
    sum =0
    for i in main_array:
        sum = sum +i
    print(sum)