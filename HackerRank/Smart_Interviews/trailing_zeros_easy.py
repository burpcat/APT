# This solution provides a solution to the problem, but one of the test case fails due to time complexity

def factorial(basic_input):
    sum = 1
    for i in range(1,basic_input+1):
        sum = sum * i
    return sum

def count_x(fact_val,basic_input):
    count =0
    iter=0
    fact_val = str(fact_val)
    main_list = list(reversed(fact_val))
    for i in main_list:
        if int(i) == 0:
            # if(iter!=0 and main_list[iter-1]==main_list[iter]):
            if(main_list[iter-1]==main_list[iter]):
                # print(main_list[iter-1],main_list[iter])
                # print(iter)
                count = count+1
        iter = iter+1
        if(int(i)!= 0):
            break
    # return (count+1)
    return count+1 if basic_input>4 else count

max_iter = int(input())

for i in range(max_iter):
    basic_input = int(input())

    fact_val = factorial(basic_input)

    count_val = count_x(fact_val,basic_input)
    print(count_val)