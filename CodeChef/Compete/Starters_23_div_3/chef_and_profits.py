basic_input = int(input())

def stock_calc(stock,buy,sell):
    profit = sell-buy
    return stock*profit

for i in range(basic_input):
    basic_list = list(map(int, input().split()))
    print(stock_calc(basic_list[0],basic_list[1],basic_list[2]))