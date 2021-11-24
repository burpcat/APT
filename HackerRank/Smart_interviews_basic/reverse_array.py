basicInput = int(input())
basicInput = input()

mainStr = ""  # Empty string for the output

# basicInput = int(5)
# basicInput = "2 19 8 15 4"

mainList = map(int, basicInput.split())
subList = list()
for i in mainList:
    # inserts every new element at the start of the array
    subList.insert(0, i)

mainStr = ' '.join([str(elem) for elem in subList])

print(mainStr)
