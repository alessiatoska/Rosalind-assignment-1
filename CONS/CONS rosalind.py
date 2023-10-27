#CONS rosalind

from Bio import SeqIO, motifs


sequence=[]


for seq_record in SeqIO.parse("CONS_rosalind.txt", "fasta"):
    sequence.append(seq_record.seq)
cons_seq= motifs.create(sequence)
matrix=cons_seq.counts

print(cons_seq.consensus)
#print(matrix)   this prints a matrix with decimal 0s and with indexes,it looks ugly

good_matrix = {}
for base, values in matrix.items():
    integer_values = [int(value) for value in values]
    good_matrix[base] = integer_values



for base, values in good_matrix.items():
    print(base + ":  " + " ".join(map(str, values)))
