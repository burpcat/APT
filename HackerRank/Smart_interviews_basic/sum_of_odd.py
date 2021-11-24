basicLen = int(input())
basicStr = input()
basicList = map(int, basicStr.split())

high_value = 0
for ele in basicList:
    if not ele % 2 == 0:
        high_value = high_value + ele       # high value is the sum of the odd numbers
    else:
        pass

print(high_value)
