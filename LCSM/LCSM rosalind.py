#LCSM rosalind

from Bio import SeqIO

dna=[]
for seq_record in SeqIO.parse("LCSM_rosalind.txt", "fasta"):
    dna.append(seq_record.seq)


def lcsm(dna):
    if not dna:
        return ""

    min_length = min(len(seq) for seq in dna)
    longest = ""

    for i in range(min_length):
        for j in range(i + len(longest) + 1, min_length + 1):
            common = dna[0][i:j]
            if all(common in seq for seq in dna):
                longest = common

    return longest
print(lcsm(dna))

