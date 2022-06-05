from Bio import Entrez, SeqIO

Entrez.email='kcc0225@naver.com'

handle= Entrez.esearch(db='nucleotide', term='CRT[Gene Name] AND "Plasmodium falciparum"[Organism]')
rec_list = Entrez.read(handle)

if rec_list['RetMax']<rec_list['Count']:
    handle=Entrez.esearch(db='nucleotide', term='CRT[Gene Name] AND "Plasmodium falciparum"[Organism]', retmax=rec_list['Count'])
    rec_list=Entrez.read(handle)

id_list=rec_list['IdList']

print(len(id_list))

hd1=Entrez.efetch(db='nucleotide',id=id_list,rettype='gb')
recs=list(SeqIO.parse(hd1,'gb'))
for rec in recs:
    if rec.name=='KM288867':
        break
print(rec.name)
print(rec.description)

