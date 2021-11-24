mainLen = int(input())
basicInput = input()
subList = list()

# using a map function to split a string and convert it into a list
basicList = map(int, basicInput.split())

for i in basicList:
    if i in subList:
        subList.remove(i)   # removes the duplicate elements
    else:
        subList.append(i)

opString = ' '.join([str(elem) for elem in subList]
                    )  # converting list to a string

print(opString)
