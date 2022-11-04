#!/bin/python3
# binning.py v1.0 written by Michael Beavitt on 04/11/2022

# importing modules
import os
import shutil

# slightly janky method of making directory names, checking if one exists already
for x in range(1,10):
    if os.path.isdir(str(x)+"00-"+str(x)+"99"):
        continue
    else:
        os.mkdir(str(x)+"00-"+str(x)+"99")

dir_names = os.

seq_file = input("please input a sequence file name...")
dna_seqs = open(seq_file).read().split()

for seq in dna_seqs:
    print(len(seq))

