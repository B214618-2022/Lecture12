#!/bin/python3

#Setting variables
DNA_source = open('./files/genomic_dna2.txt')
concatenated_exons = open('catexons.txt', 'w')
exon_coords = open('./files/exons.txt')

for line in exon_coords:
    print(line)
