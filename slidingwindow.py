#!/bin/python3
# slidingwindow.py written by Michael Beavitt on 01/11/2022

from subprocess import check_output

sequence = []

AJ223353_seq = check_output(["efetch", "-db", "nucleotide", "-id", "AJ223353", "-format", "fasta"]).decode("UTF-8")
seqlist = AJ223353_seq.split('\n')
for x in seqlist:
    if not x.startswith(">"):
        sequence.append(x)

newseq = ''.join(sequence)

