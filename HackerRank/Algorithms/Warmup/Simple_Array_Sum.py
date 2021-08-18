# Can be optimised much more effeciently

banum = int(input())
list1 = input().split()
sum = 0
list1 = map(int, list1)

for num in list(list1):
    sum += int(num)

print(sum)
