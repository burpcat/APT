# https://www.codechef.com/START24C/problems/EVMHACK

# Approach

# we can hack only one EVM at a times 
# so , from the total attained votes, we remove the number of votes we got, and then add the total number of votes at the poll
# so in total, we can estimate whether we can win or not

basic_input = int(input())

def win_or(a,b,c,p,q,r):

    total_list = [p,q,r]
    got_list = [a,b,c]

    win_count = (p+q+r)/2

    acquired = a+b+c

    if not(acquired>win_count):
        for i in range(3):

            if((acquired-got_list[i])+total_list[i] > win_count):
                return 'YES'
        
        return 'NO'

    return 'YES'
        

for i in range(basic_input):
    main_list = list(map(int, input().split()))
    print(win_or(main_list[0],main_list[1],main_list[2],main_list[3],main_list[4],main_list[5]))