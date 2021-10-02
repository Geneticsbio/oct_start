seq="AATGATGATaatTAG"
#upper()==>concert sequence to upper case
print(seq.upper())
#lower()==convert sequence to lower case
print(seq.upper())
#count() ==gives you the count of chars
seq="ATGCC"
print(seq.count("A"))
print(seq.count("c"))
print(seq.count("CC"))
#find()**>to find firdt occurence of character

# replace ()==> to replace a character with any specific character
#[::-1]==> to reverse the sequence
seq="ATGC"
gc_percent=100*(seq.count("G")+seq.count("c"))/len(seq)
print(gc_percent)
seq="ATGTATAGTAGATAATTGT"
print(seq.find("A"))
print(seq.find("T"))
print(seq.find("ATAATTGT"))

dna_Seq="attgatattatgtaa"
res_enz_site="atgt"
print(dna_Seq.find(res_enz_site))
#replace()==> to replace a character with any specific character
seq="ATTT"
print(seq.replace("A","N"))
seq="ATTT"
print(seq.replace("T","A"))
#[::-1]==>to reverse the sequence
dna_seq="atgc"
print(dna_seq[::-1])