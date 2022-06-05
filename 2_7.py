from collections import defaultdict
import re
import HTSeq

lct_bed = HTSeq.BED_Reader('LCT.bed')

feature_type=defaultdict(int)

for rec in lct_bed:
    last_rec = rec
    feature_type[re.search('([A-Z]+)',rec.name).group(0)]+=1

print(feature_type)
