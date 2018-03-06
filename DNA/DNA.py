#Rosalind #DNA

def dna_base_count(dna_string):
    ACGT = [0,0,0,0]

    DNA = True
    
    for base in dna_string:
        if base == 'A':
            ACGT[0] += 1
        elif base == 'C':
            ACGT[1] += 1
        elif base == 'G':
            ACGT[2] += 1
        elif base == 'T':
            ACGT[3] += 1
        else:
            DNA = False

    if DNA == True:
        print(*ACGT)
    else:
        print("input is not DNA")

file = open("input.txt", "r")

test_string = file.read().strip()
 
file.close()

dna_base_count(test_string)
