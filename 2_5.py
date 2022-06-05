from Bio import SeqIO
from collections import defaultdict

recs = SeqIO.parse(open('SRR003265_1.filt.fastq','rt',encoding='utf-8'),'fastq')

cnt=defaultdict(int)

for rec in recs:
    for letter in rec.seq:
        cnt[letter]+=1
        print(cnt[letter])
tot=sum(cnt.values())
print(tot)
for letter, cnt in cnt.items():
    print('%s : $.2f %d' % (letter,100.*cnt/tot,cnt) )
