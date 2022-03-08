# https://codeforces.com/contest/1650/problem/A
#

def checker(main,sample):
    i =1
    for ele in main:
        #print(i,ele,sample)
        if((i%2!=0) and (ele == sample)):
            return 'YES'
        i+=1
    
    return 'NO'

basic_input = int(input())

for i in range(basic_input):
    main_str = input()
    sample = input()

    print(checker(main_str,sample))