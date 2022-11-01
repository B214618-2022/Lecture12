#!/bin/python3

oldfile = open("files/input.txt")
newfile = open("trimmedseqs.txt", "w")

for x in oldfile:
    seq = x[14:]
    newfile.write(seq)
    print(len(seq))

oldfile.close()
newfile.close()
