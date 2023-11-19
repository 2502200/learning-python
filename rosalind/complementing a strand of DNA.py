s = "AAAACCCGGT"
sc = " "

for letter in s:
    if letter == "A":
        sc += "T"
    elif letter == "T":
        sc += "A"
    elif letter == "C":
        sc += "G"
    elif letter == "G":
        sc += "C"

print(sc)


#not sure how to reverse it