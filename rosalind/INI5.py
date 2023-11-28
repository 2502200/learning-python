#required output: file containing even-numbered lines from the original file by assuming 1-based numbering
#opening the file in read mode
f = open('filename', 'r')
filelist = []
linelist = []

#looping over a file and appending its lines to a list
for s in f:
    filelist.append()

#range from 1 to the enitre length of a list, since the numbering is 1-based
for lines in range(1, len(filelist)):
#using modulo operator to check if the lines are odd (since it's 1-based numbering)
    if lines % 2 == 1:
        linelist.append(filelist[lines])
#appending lines to a list and printing a list without square brackets using a '*'
print(*linelist)

f.close()
