# https://www.codechef.com/problems/MTYFRI

def score_check(some_list):
    score = 0
    for ele in some_list:
        score += ele
    
    return score


def checker(main_list,n,k):
    
    motu = []
    tomu = []


    for i in range(len(main_list)):
        if (i%2!=0):
            tomu.append(main_list[i])
        else:
            motu.append(main_list[i])
    
    #print(motu,tomu)
    motu.sort()
    motu.reverse()
    tomu.sort()
    #print(motu,tomu)

    motu_s = score_check(motu)
    tomu_s = score_check(tomu)
    
    i = 0
    for x in range(k):
        #motu[x], tomu[x] = tomu[x], motu[x]
        temp = motu[x]
        motu[x] = tomu[x]
        tomu[x] = temp

        motu_s = score_check(motu)
        tomu_s = score_check(tomu)

        if(tomu_s > motu_s):
            return 'YES'
    return 'NO'


basic_input = int(input())

for _ in range(basic_input):
    
    #n,k = list(map(int,input().split()))
    main_vars = list(map(int,input().strip().split()))
    main_list = list(map(int,input().strip().split()))

    print(checker(main_list,main_vars[0],main_vars[1]))