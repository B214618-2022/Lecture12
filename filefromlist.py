#!/bin/python3

somecolours4 = ['blue','red','green']

for colour_item in somecolours4:
    myfile = open(colour_item + '.txt', 'w')
    myfile.write(str(len(colour_item)) + '\n')
    myfile.close()
    print(f'{colour_item[0:3].upper()}')
