old_list = [4,6,9,7,34,87,12,3]
def buble_sort(my_list):
    amount = len(my_list)-1
    for n in range(0, amount):
        for x in range(0,amount):
            if my_list[x] > my_list[x+1]:
                my_list[x], my_list[x+1] = my_list[x+1], my_list[x]
    return my_list
    
print("old list:", old_list)
newList = buble_sort(old_list).copy()
print('New List:', newList)
