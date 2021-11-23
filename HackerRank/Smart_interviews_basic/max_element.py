totalNum = int(input())  # we ignore this input
basicInput = input()  # we convert the string to a list
mainList = map(int, basicInput.split())

print(max(mainList))
