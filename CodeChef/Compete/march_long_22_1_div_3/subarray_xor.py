# https://www.codechef.com/MARCH221C/problems/SUB_XOR

# logic works, but has time complexity issues, needs better implementation

def checker(a):

    main_list = []

    for n in range(1,len(a)+1):
        for i in range(0,len(a)):
            value = a[i:i+n]
            if(len(value)==n): # in case of odd numbers we dont want to append the last digits
                main_list.append(int(value,2))

    print(main_list)
    # xor operation on individual elements now

    xor_val = 0 # initial value will be one since, x ^ 0 =0 ; x ^ 1 = 1
    for j in range(len(main_list)):
        xor_val ^= main_list[j]
    
    print(xor_val)

basic_input = int(input())

for _ in range(basic_input):
    
    bin_num_len = int(input())
    bin_num = input()

    checker(bin_num)
