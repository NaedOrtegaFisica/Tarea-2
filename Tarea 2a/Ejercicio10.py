def doors_game(tries, doors):
    from random import randint
    Win = 0
    Lose = 0 

    for x in range(tries):
        m = randint(0,doors-1)
        shuffle_doors = [0 for i in range(0,m)] + ["P"] + [0 for i in range(m,doors-1)]

        n = randint(0,doors-1)
        if shuffle_doors[n] == "P":
            Lose = Lose + 1
        elif shuffle_doors[n] == 0:
            Win = Win + 1

    return f"You lose {Lose} times, and win {Win} times in {tries}, and in {doors} doors" ,shuffle_doors
    

print(doors_game(1000,5))
