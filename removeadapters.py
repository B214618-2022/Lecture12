#!/bin/python3

#Setting variables
count=0
my_file = open('./files/input.txt')
new_file = open('trimmed.txt', 'w')


for eachline in my_file :
    count+=1 
    adapterfree = eachline[14:] # Removing the adapters
    len_af = len(adapterfree) # Finding the new length
    print(f'The length of sequence  {count}  is  {len_af}')
    new_file.write(adapterfree + '\n') # Writing the new adapters to a file

new_file.close() # Closing the connection to the new file
