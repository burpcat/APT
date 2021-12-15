# https://www.hackerrank.com/contests/smart-interviews-basic/challenges/si-basic-linear-search-on-array
# Smart search Basic > Linear Seardch on a Array


basic_input = list(map(int,input().split()))
basic_list = list(map(int,input().split()))
count =0;


for ele in basic_list:
    if basic_input[1] == ele:
        print(count)
    count= count+1