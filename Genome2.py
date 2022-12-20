# 檔案讀取
def readGenome(filename):
    genome = ''
    with open(filename, 'r') as f: 
        for line in f: 
            if not line[0] == '>': 
                genome += line.rstrip() 
    return genome

file = readGenome("GCF_000157115.2_Escherichia_sp_3_2_53FAA_V2_genomic.fna")
print("\n讀取資料型態為:",type(file))

def reverseComplement(s):
    complement = {'A':'T', 'C':'G', 'G':'C', 'T':'A'} 
    t = ''
    for base in s:
        t = complement[base] + t
    return t

print()
print(file[:10])
print(reverseComplement(file[:10]))

counts = {'A':0, 'T':0, 'G':0, 'C':0 ,'N':0}
for base in file:
    counts[base] += 1
print(counts,"\n")
