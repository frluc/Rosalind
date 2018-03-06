#Rosalind #GC

def parse(fasta, sequences):
    input_file = open(fasta, "r")
    for line in input_file:
        if line.startswith(">"):
            name = line[1:].strip()
            sequences[name] = ""
        else:
            sequences[name] += line.strip()
    input_file.close()

def seq_gc(seq):
    gc = (seq.count("G") + seq.count("C"))/float(len(seq))
    return gc

sequences = {}

parse("fasta.txt",sequences)

gc_content = {}

for key in sequences:
    gc_content[key] = seq_gc(sequences[key])

max_gc_value = max(gc_content.values())
max_gc_key = ""

for key in gc_content:
    if gc_content[key] == max_gc_value:
        max_gc_key = key

print(max_gc_key)
print(round(max_gc_value, 6)*100)
