def blood_count(archive):
    list = []
    list2 = []
    AB_count = 0
    B_count = 0
    A_count = 0
    O_count = 0
    with open(archive) as f:
        read = f.read()
        for x in read:
            if x == '\ufeff':
                continue
            else:
                list = list + [x]
    len_list = range(0,len(list))
    for n in len_list:
        if list[n] == "A" and list[n+1] == "B":
            list2 = list2 + ["AB"]
            AB_count = AB_count + 1
        elif list[n] == "A" and list[n+1] == " ":
            list2 = list2 + ["A"]
            A_count = A_count + 1
        elif list[n] == "B" and list[n-1] == " ":
            list2 = list2 + ["B"]
            B_count = B_count + 1
        elif list[n] == "O":
            list2 = list2 + ["O"]
            O_count = O_count + 1

    return print(f'''Hay {AB_count} con tipo de sangre AB
Hay {A_count} con tipo de sangre A
Hay {B_count} con tipo de sangre B
Hay {O_count} con tipo de sangre O''')

blood_count("bloodtype1.txt")