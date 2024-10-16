
def blood_count(archive):
    list = {}
    with open(archive) as f:
        read = f.read()
        for x in read.split():
            if x == "\ufeffAB":
                list['AB'] = 1
            elif x == 'ï»¿AB':
                list['AB'] = 1
            elif x in list:
                list[x] += 1
            else:
                list[x] = 1
        return list


print(blood_count("bloodtype1.txt"))