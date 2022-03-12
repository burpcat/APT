# https://www.codechef.com/problems/NAME1

from collections import Counter

def checker(parents,child_count):
    
    children = ""
    for _ in range(int(child_count)):
        children += input()

    parent_counter = Counter(parents)   # This method returns a dictionary / unordered hashamp of all the elements
    children_counter = Counter(children)

    if (children_counter - parent_counter):  # if this value turns positive, then there are more characters inside 
        print('NO')                         # children_counter than parent_counter, which means children is not a substring
    else:                                   # of parent string.
        print('YES')

basic_input = int(input())

for _ in range(basic_input):

    parent1,parent2 = map(str,input().split())
    parents = parent1 + parent2

    child_count = input()
    checker(parents,child_count)