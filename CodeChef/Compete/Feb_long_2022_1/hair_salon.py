#https://www.codechef.com/FEB221C/problems/CHEFBARBER

basic_input = int(input())

def wait_time(custo,time):
    print(custo*time)


for i in range(basic_input):
    
    main_list = list(map(int,input().split()))
    custo, time = main_list[0],main_list[1]
    wait_time(custo,time)