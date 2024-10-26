



def collatz(n):
    def g(n):
        m = n/2
        if m == 1:
            return int(m)
        else:
            return collatz(m)
    def h(n):
        s = 3 * n +1
        return collatz(s)
    
    print(int(n))
    if n % 2 == 0:
        return g(n) 
    elif n % 2 != 0:
        return h(n)

print(collatz(6))