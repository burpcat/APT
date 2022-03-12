# https://www.codechef.com/problems/SLAB

def checker(init_amount):

    tax = 0

    while(True):
        if(init_amount> 250000):
            tax+= ((min(init_amount,500000)-250000)*0.05)
        if(init_amount>500000):
            tax+= ((min(init_amount,750000)-500000)*0.10)
        if(init_amount>750000):
            tax+= ((min(init_amount,1000000)-750000)*0.15)
        if(init_amount>1000000):
            tax+= ((min(init_amount,1250000)-1000000)*0.20)
        if(init_amount>1250000):
            tax+= ((min(init_amount,1500000)-1250000)*0.25)
        if(init_amount>1500000):
            tax+= (init_amount-1500000)*0.30
        
        break
    
    return tax



    

basic_input = int(input())


for _ in range(basic_input):
    init_amount = int(input())
    tax = checker(init_amount)
    print(int(init_amount-tax))