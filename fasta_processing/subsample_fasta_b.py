from Bio import SeqIO
from random import sample
with open("/path/to/your/fasta.fasta") as f:
    seqs = SeqIO.parse(f,"fasta")
    subsampled = ((seq.name, seq.seq) for seq in  sample(list(seqs),20)) #specify the number of randomly sampled sequences here 20

print subsampled

with open("/output/path/subsampled.fasta", "wb") as o:
    for record in subsampled:
        print record
        o.write(">{}\n{}\n".format(*record))

