
def frequency1(string):
    variables = {}
    for x in "abcdefghijklmnñopqrstuvwxyz":
        variables[x] = 0

    for x in string:
        if x == " ":
            continue
        else:
            variables[x.lower()] += 1

    return print(variables.values())

frequency1("The quick red fox got bored and went home")


