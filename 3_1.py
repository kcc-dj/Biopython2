
from Bio import SeqIO,SeqUtils
genome_name='PlasmoDB-9.3_Pfalciparum3D7_Genome.fasta'
recs=SeqIO.parse(genome_name,'fasta')
#for rec in recs:
#    print(rec.description)
chrom_sizes={}
chrom_GC={}
block_size=50000
min_GC=100.0
max_GC=0.0

for rec in recs:
    if rec.description.find('SO=chromosome')==-1:
        continue
    chrom = int(rec.description.split('_')[1])
    chrom_GC[chrom]=[]
    size=len(rec.seq)
    chrom_sizes[chrom]=size
    num_blocks=size//block_size + 1
    for block in range(num_blocks):
        start = block_size*block
        if block==num_blocks -1 :
            end = size
        else:
            end=block_size+start+1
        block_seq=rec.seq[start:end]
        block_GC=SeqUtils.GC(block_seq)
        if block_GC<min_GC:
            min_GC=block_GC
        if block_GC>max_GC:
            max_GC=block_GC
        chrom_GC[chrom].append(block_GC)
        print(min_GC,max_GC)

