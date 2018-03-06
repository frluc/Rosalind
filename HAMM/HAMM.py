#Rosalind #HAMM

def hamming_distance(dna1, dna2):
    dh = 0
    if len(dna1) != len(dna2):
        print("DNAs not of equal length")
    else:
        for i in range(0,len(dna1)):
            if dna1[i] != dna2[i]:
                dh += 1
        return dh

input_file = open("input.txt","r")

dna1 = input_file.readline().strip()
dna2 = input_file.readline().strip()

input_file.close()

print(hamming_distance(dna1,dna2))
