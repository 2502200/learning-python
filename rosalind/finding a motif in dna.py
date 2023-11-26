#two dna sequences are given
dnaseq = 'GATATATGCATATACTT' 
#subseq is a substring with several locations inside a 'dnaseq'(main string)
subseq = 'ATAT'

locations = []

for items in range(0, len(dnaseq)):
#to check the presence of the subsequence within the main sequence, from the 'items' as the start parameter    
    if dnaseq.startswith(subseq, items):
#adding +1, since python has 0-based indexing, and this exercise requires 1-based indexing        
        locations.append(items + 1)

#to print a list wihout the square brackets '*' is used
print(*locations)        
      
