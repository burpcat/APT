# https://www.hackerrank.com/contests/smart-interviews-basic/challenges/si-basic-reverse-string
# Smart interviews Basic > Reverse String 

basic_input = input()
sub_list = list()


for letter in basic_input:
    sub_list.insert(0,letter)
    
newlist = ''.join([elem for elem in sub_list])

#newlist = ''.join(sub_list)  # This can also be used

print(newlist)
