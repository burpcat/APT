# https://www.codechef.com/FEB221C/problems/BINBASBASIC
# wrong answer was the validator output

basic_input = int(input())

def pal_check(count,leng,main_str):
    sublist1 = []
    sublist2 = []
    i =0
    for ele in main_str:
        if (i<leng//2):
            sublist1.append(int(ele)) # dividing the string into two pieces
        elif(i>leng/2):
            sublist2.append(int(ele)) # adding a case for odd nums
        elif(i==leng//2 and leng%2==0):
            sublist2.append(int(ele))
        else:
            i+=1
        i+=1

    # print(sublist1,sublist2)

    num_count =0
    if count == 0:
        return 'NO'
    else:
        for i in range(leng//2):
            # print(sublist1[i])
            # print(sublist2[-i-1])
            if ((sublist1[i] ^ sublist2[-i-1])!=0): 
                num_count+=1
    
    if(num_count>count):
        return 'NO'
    else:
        return 'YES'

for i in range(basic_input):
    main_list = list(map(int, input().split()))
    leng,count = main_list[0],main_list[1]
    main_str = input()
    print(pal_check(count,leng,main_str))