sequence = 'ATGC'
print("\n讀取資料型態為:",type(sequence))

# 字串操作
# print(sequence[0:2])
# for s in sequence:
#     print(s)

#建立亂數鹼基對
import random
def randomDnaSeqs(base_number):
   seqs = ''
   for _ in range(base_number):
       seqs += random.choice('ATGC')
   return seqs
RandomGenome = randomDnaSeqs(10)
print("\n建立一個亂數鹼基對(長度為10):\t",RandomGenome)

#建立互補函式
def reverseComplement(s):
    complement = {'A':'T', 'C':'G', 'G':'C', 'T':'A'} 
    t = ''
    for base in s:
        t = complement[base] + t
    return t
print("\t互補結果:\t\t",reverseComplement(RandomGenome))

#計算鹼基對數量
def count(a):
    counts = {'A':0, 'T':0, 'G':0, 'C':0}
    for base in a:
        counts[base] += 1
    return counts

print(count(RandomGenome))
print(count(reverseComplement(RandomGenome)))