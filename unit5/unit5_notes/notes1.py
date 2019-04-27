"""

FINAL PROJECTS

start thinking about final project

stand alone application

presentation
what achieved
what attempted
what was diffcult
what you did to overcome

meant to be a project that one can share with the world to show your skills

https://any-api.com/

examples of his crawler to pull data down.

https://raw.githubusercontent.com/sureshmelvinsigera/LinkedInParser/master/LinkedInParser.py

TWITTER API also quite handy and would be good to work with

"""

"""
creating files, accessing files

files can become objects

"""
#I/O = input/output

##opening the file in read only mode

#FOR NOW, FILE IN SAME DIRECTORY AS SCRIPT,
#if not we would have to learn how to put the full path not in scope for today's lesson
#FOR NOW HAS TO BE A TXT FILE
#out of the scope for today's lesson - next week work with excel in and csv, need pandas library for that


input_file = open("data.txt", "r")  #open a file, need name of the file, need mode in this case r = read only mode
print(input_file) #prints the input file, #wont get the content of the file, returns files
print(type(input_file)) #give the class type
#if you don't close the file, it will stay open in memory
#every time you open a file, make sure you close it
input_file.close() #close the file

#r = read only on an existing file



"""
results - the object of the file
<_io.TextIOWrapper name='data.txt' mode='r' encoding='UTF-8'>
<class '_io.TextIOWrapper'>


encoding = 'UTF-8'
talks about the format of the data, unit code text, each character has a numeric code speak

UTF is how you get to the unicode (computer code) how they are stored, 
hex ids for all types of letters in various languages
mathematical symbols

"""






