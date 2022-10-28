#!/bin/python3

count=0
my_file = open('./files/input.txt')

for eachline in my_file :
    count+=1
    adapterfree = eachline[14:]
    len_af = len(adapterfree)
    print(f'The length of sequence  {count}  is  {len_af}')
    
#    print('We are processing line {} of the file'.format(count))
#    print(f'There are {line_length} characters on the line')


#for colour_item in somecolours4 :
#    myf = open(colour_item + '.txt', 'w')
#    myfile.write(str(len(colour_item)) + '\n')
#    myfile.close()
#    f'{colour_item[0:3].upper()}'
