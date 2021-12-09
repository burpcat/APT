# https://www.hackerrank.com/contests/smart-interviews-basic/challenges/si-basic-print-multiplication-table
# Smart Interviews Basic > Print multiplication table

basic_input = input()


for i in range(1,11):
    print(f'{int(basic_input)} * {i} = {int(basic_input)*i}')