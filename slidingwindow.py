#!/bin/python3
# slidingwindow.py written by Michael Beavitt on 01/11/2022

from subprocess import check_output

sequence = []

AJ223353_seq = check_output(["efetch", "-db", "nucleotide", "-id", "AJ223353", "-format", "fasta"]).decode("UTF-8")
seqlist = AJ223353_seq.split('\n')
for x in seqlist:
    if not x.startswith(">"):
        sequence.append(x)

new_seq = ''.join(sequence)

window = 30
offset = 3
seq_len = len(new_seq)
start_point = 0
end_point = window
kmer_id = 1

kmerfile = open("kmers.txt", "w")

while start_point < len(new_seq):
    kmer = new_seq[start_point:end_point]
    kmer_len = len(kmer)
    content_g = kmer.upper().count('G')
    content_c = kmer.upper().count('C')
    gc_proportion = round((content_g + content_c) / kmer_len, 2)
    header = ">" + "kmer " + str(kmer_id) + ", GC content - " + str(gc_proportion)
    kmerfile.write(header + "\n" + kmer + "\n")
    start_point = start_point + offset
    end_point = end_point + offset
    kmer_id = kmer_id + 1

kmerfile.close()
