def fileLenght(Document):
    Lenght = 0
    try:
        with open(Document) as file:
            for x in file.read():
                if x == " ":
                    continue
                elif x == "\uffef":
                    continue
                else:
                    Lenght = Lenght + 1
        return Lenght
    except FileNotFoundError:
        return "Im sorry, the file is not found!!"

    

print(fileLenght("bloodtype.txt"))