import pysam

bam=pysam.AlignmentFile('NA18489.bam','rb')

headers=bam.header

for record_type, records in headers.items():
    print(record_type)
    for i , record in enumerate(records):
        if type(record)==dict:
            print('\t%d' % (i+1))
            for field, value in record.items():
                print('\t\t%s\t%s' % (field,value))
        else:
            print('\t\t%s' % record)
