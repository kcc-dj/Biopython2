from Bio import SeqIO

recs = SeqIO.parse('example.fasta','fasta')

for rec in recs:
    seq=rec.seq
    print(rec.description)
    print(seq[:10])
   # print(seq.alphabet)
