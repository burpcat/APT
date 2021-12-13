sams_loc = list(map(int,input().split()))
sams_list = list(range(sams_loc[0],sams_loc[1]))

tree_loc = list(map(int,input().split()))

fruit_quan = list(map(int,input().split()))

apple_dist = list(map(int,input().split()))

orange_dist = list(map(int,input().split()))



apple_count = 0
orange_count = 0

for ele in apple_dist:
    if((ele+tree_loc[0]) in sams_list):
        apple_count = apple_count +1

for i in orange_dist:
    if((i+tree_loc[1]) in sams_list):
        orange_count = orange_count +1

print(apple_count)
print(orange_count)
