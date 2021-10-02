seq="ATGCATGCA"

# A   1   2   3   4   5   6   7   8
# *   |   |   |   |   *   *   *   *
#['A','T','G','C','A','T','G','C','A']

#Slicing
#string_name[start:stop]==> returns the part of string from start index to stop-1 index

print(seq[1:5])
print(seq[2:5])
print(seq[3:5])
print(seq[4:5])

print(seq[4:7])
print(seq[-5:-2])
print(seq[-9:-6])
#string_name[:]=string_name
print(seq[2:])
print(seq[:-2])

dna_seq="ATGATAGTAGTAGAGATA"
length=len(dna_seq)
print(seq[:int(length/2)])
print(seq[int(length/2):])