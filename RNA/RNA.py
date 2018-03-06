#Rosalind #RNA

def dna_to_rna(dna_string):
	
    return dna_string.replace("T","U")


file = open("input.txt", "r")

test_string = file.read().strip()

file.close()

print(dna_to_rna(test_string))

file = open("output.txt", "w")

file.write(dna_to_rna(test_string))

file.close()
