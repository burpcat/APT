basic_input = int(input())
basic_len = len(str(basic_input))
sum = 0


for i in range(basic_len):
    temp = (basic_input % 10)
    temp = int(temp)
    sum = sum + temp
    basic_input = (basic_input/10)

print(sum)
