# https://www.codechef.com/START24C/problems/AVOIDCONTACT

# Approach

    # first sort out all the unaffected in the first few rooms
    # then every infected gets a room + empty adjacent room (so 2x rooms for infected)
    # if the total and affected are equal, then they get total + total-1 rooms 
        # since the first one doesnt need empty on both sides

basic_input = int(input())

def contact_check(total,infected):
    count = 0                    # total no of rooms required
    count = total-infected
    if (count ==0):
        count = infected + (infected-1)
    else:
        count += infected*2
    print(count)


for i in range(basic_input):
    stu_list = list(map(int, input().split()))
    contact_check(stu_list[0],stu_list[1])