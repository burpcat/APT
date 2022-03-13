# https://www.codechef.com/problems/CHEFA

basic_input = int(input())

def checker(pile_list,n):

    chef_score = 0
    roma_score = 0

    pile_list.sort()
    pile_list.reverse()

    for i in range(n):
        if i%2==0:
            chef_score += pile_list[i]
        else:
            roma_score += pile_list[i]
    
    print(chef_score)

for _ in range(basic_input):
    
    num_of_piles = int(input())
    pile_list = list(map(int, input().split()))

    checker(pile_list,num_of_piles)


# logic 
# if the piles are sorted in a reverse order, since chef has the first turn, every alternate pile
# he will try to take to maximise his score