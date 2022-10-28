#!/bin/python3

count=0
my_file = open('./files/input.txt')
new_file = open('trimmed.txt', 'w')

for eachline in my_file :
    count+=1
    adapterfree = eachline[14:]
    len_af = len(adapterfree)
    print(f'The length of sequence  {count}  is  {len_af}')
    new_file.write(adapterfree + '\n')

new_file.close()
