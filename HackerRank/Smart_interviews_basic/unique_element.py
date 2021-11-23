# mainLen = int(input())
# basicInput = input()
mainLen = int(7)
basicInput = "5 4 10 9 21 4 10"

# using a map function to split a string and convert it into a list
basicList = map(int, basicInput.split())

for i in range(mainLen):
    print(basicInput)
