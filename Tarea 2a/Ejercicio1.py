
def remuve_duplicates(list):
    clear_list = []
    for x in list:
        if x in clear_list:
            continue
        else:
            clear_list = clear_list + [x]
    return clear_list

list_1 = [1,1,2,3,4,1,2,3]
list_2 = [7,5,3,5,1]
list_3 = [1,1,1,1]

print(remuve_duplicates(list_1))
print(remuve_duplicates(list_2))
print(remuve_duplicates(list_3))


     



           
