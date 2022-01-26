

basic_input = int(input())

def check_func(basic_list,len_of_ar):
    basic_list.sort()
    basic_list.append('x') # we add this to prevent list index out of range
    res_list = []
    for i in range(len_of_ar):
        if basic_list[i] == basic_list[i+1]:
            res_list.append(basic_list[i])
    
    print(int(res_list[0]),int(res_list[1]))
for i in range(basic_input):
    len_of_ar = int(input())
    basic_list = list(map(int,input().split()))
    
    check_func(basic_list,len_of_ar)