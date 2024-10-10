def dolar_to(Divisa, Dollars):
    all_list = []
    Divisa_name = []
    Change = []

    with open("currencies.txt") as f:
        for x in f.read().splitlines():
            all_list = all_list + [x]
        n = range(len(all_list))

        for m in n:
            if all_list[m][0] == '\ufeff':
                Divisa_name = Divisa_name + [all_list[m][1:4]]
            else:
                Divisa_name = Divisa_name + [all_list[m][0:3]]

        for m in n:
            object = ""
            for s in range(len(all_list[m])):
                if all_list[m][s] in ["1","2","3","4","5","6","7","8","9","0","."]:
                    object = object + all_list[m][s]
            else:
                Change = Change + [float(object)]
        
        m = range(len(Divisa_name))

        for x in m:
            if Divisa_name[x] == Divisa:
                return print(f"{Dollars} dollars are {Change[x]*float(Dollars)} {Divisa}")
                break   




dolar_to("AUD",100)
