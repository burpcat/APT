# https://www.codechef.com/MARCH221C/problems/WORDLE

def checker(S,T):

    M = ""

    for i in range(5): # given that both will always have a length of 5
        if (S[i]==T[i]):
            M += 'G'
        else:
            M += 'B'
    
    return M




basic_input = int(input())

for _ in range(basic_input):
    hidden = input()
    guess = input()
    print(checker(hidden,guess))
