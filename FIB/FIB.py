# Rosalind #FIB

def fibonnaci_rabbits(n, k):
    i = 0
    j = 1
    for x in range(0,n):
        tmp = i * k + j
        i = j
        j = tmp
    return i

n = int(input("n = "))

k = int(input("k = "))

print("FIB = "+str(fibonnaci_rabbits(n,k)))
