# https://www.hackerrank.com/contests/smart-interviews/challenges/si-lcm-and-hcf/problem
# Smart interviews > LCM & HCF


iterations = int(input())

def hcf(big_num,small_num):
    remainder = int()
    remainder = big_num % small_num

    while(remainder > 0):
        spare_var = remainder     # using a spare variable to fix overwriting the previous number
        remainder = small_num%remainder
        small_num = spare_var     # rewriting the small_num variable for further dividing

    return small_num

def lcm(big_num,small_num,hcf_res):
    result = small_num // hcf_res
    return (result*big_num)

for i in range(iterations):
    basic_input = list(map(int,input().split()))
    if(basic_input[0]>basic_input[1]):
        big_num = basic_input[0]
        small_num = basic_input[1]
    else:
        big_num = basic_input[1]
        small_num = basic_input[0]

    hcf_res = hcf(big_num,small_num)
    lcm_res = lcm(big_num,small_num,hcf_res)

    print(lcm_res,hcf_res)



# Referred Articles of Information
# for LCM : https://mathchat.me/2010/09/07/how-to-find-the-lcm-fast/
# for HCF : https://byjus.com/maths/prime-factorization-of-hcf-and-lcm/