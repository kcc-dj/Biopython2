from Bio import SeqIO

recs = SeqIO.parse(open('SRR003265_1.filt.fastq','rt',encoding='utf-8'),'fastq')
rec=next(recs)

print(rec.id,rec.description,rec.seq)
print(rec.letter_annotations)
