#!/bin/python3

#Setting variables
somecolours4 = ['blue','red','green']


for colour_item in somecolours4:
    myfile = open(colour_item + '.txt', 'w') #creating a .txt file and naming it the correct colour
    myfile.write(str(len(colour_item)) + '\n') #writing the length of the string to the file
    myfile.close() #closing the file
    print(f'{colour_item[0:3].upper()}') #printing the first three letters of the colour in uppercase

