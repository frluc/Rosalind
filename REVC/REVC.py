#Rosalind #REVC

def dna_rev_comp(dna_string):

    rev_complement = ""

    for base in dna_string[::-1]:
        if base == "A":
            rev_complement += "T"
        elif base == "C":
            rev_complement += "G"
        elif base == "G":
            rev_complement += "C"
        elif base == "T":
            rev_complement += "A"
	
    return rev_complement

file = open("input.txt", "r")

test_string = file.read().strip()

file.close()

print(dna_rev_comp(test_string))

file = open("output.txt", "w")

file.write(dna_rev_comp(test_string))

file.close()
