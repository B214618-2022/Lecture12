#!/bin/python3

# Opening the sequence file, removing the trailing newline character and writing to a variable
myfile = open("files/genomic_dna2.txt").read().strip('\n')
# Opening a connection to the exons file
exons = open("files/exons.txt")
# Creating an empty coordinates list variable
coords = []
newfile = open("catexons.txt", "w")


# Iterating through the exons file without saving it to a variable
for x in exons:
#     Splitting by newline
    coords = x.split()
#     Splitting each coordinate entry by comma, giving a list of 2
    coords = coords[0].split(",")
#     Setting start and stop coordinates
    openexon = int(coords[0])
    closedexon = int(coords[1])
#     Retreiving the correct sequences from the file
    exon = myfile[openexon-1:closedexon]
    newfile.write(exon)

