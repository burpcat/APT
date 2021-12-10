# incomplete code - fetched only 10 points

# https://www.hackerrank.com/contests/smart-interviews-basic/challenges/si-basic-number-of-multiples
# Smart Interviews Basic > Number of multiples

basic_input = input()
count = 0
blankset = set()

for i in range(1,100000):
    if( (3*i) <=int(basic_input)):
        # print(3*i)
        count = count +1
        blankset.add(3*i)
    else:
        break

for i in range(1,100000):
    if ((5*i)<= int(basic_input)):
        # print(5*i)
        count = count +1
        blankset.add(5*i)
    else:
        break
    

# print(count)
# print(blankset)
print(len(blankset))