# https://leetcode.com/contest/weekly-contest-278/problems/keep-multiplying-found-values-by-two/
#5993. Keep Multiplying Found Values by Two

basic_input = input()
original = int(input())

def multi_func(main_list,number):
    
    while True:
        if (number in main_list):
            number *= 2
        else:
            break
    
    print(number)


multi_func(list(map(int,basic_input.split())),original)