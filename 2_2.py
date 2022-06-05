from Bio import Entrez, SeqIO

Entrez.email='kcc0225@naver.com'
hd1=Entrez.efetch(db='nucleotide',id=['NM_002299'],rettype='fasta')
seq=SeqIO.read(hd1,'fasta')
w_hd1=open("example.fasta",'w')

w_seq=seq[11:5795]
SeqIO.write([w_seq],w_hd1,'fasta')
w_hd1.close()
