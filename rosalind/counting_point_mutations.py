#s = 'GAGCCTACTAACGGGAT'
#t = 'CATCGTAATGACGGCCT'
#to count point mutations defined by hamming distance (dh)



#defina a compare function for the two dna sequences, s and t
def compare(s, t):
    dh = 0
    s = 'GAGCCTACTAACGGGAT'
    t = 'CATCGTAATGACGGCCT'
#if any letter in a seq s doesn't equal to any letter in a seq t:
#add 1 to the dh variable
    for letter in range(len(s)):
        if s[letter] != t[letter]:
            dh += 1            
    return(dh)

compare(s, t) 


