basic_input = int(input())

def avg_func(mean):
    req = mean*3
    a1 = 1
    req = req - a1
    if (req%2 ==0):
        a2 = req/2
        a3 = req/2 
        a2+=1
        a3-=1
    else:
        a2 = req/2
        a3 = a2+1 


    print(a1,int(a3),int(a2))

for i in range(basic_input):
    mean = int(input())
    avg_func(mean)