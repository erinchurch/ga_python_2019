"""

r = read only

w = open for writing

a = open for appending

b = binary mode, means true of false, like a grayscale image is binary,
     image processing would be in binary mode


t = text mode (default), by default you call it when you do 'r'

'+' open a file for a reading AND writing


"""


#WRITING TO A FILE

def write_data(file_name, text):
    file = open(file_name, 'w')  #open object, it is also called a 'buffer' in write mode, so it doesn't matter the file doesn't already exist

    try:
        file.write(text)  #asking to write the file, may or may not fail

    except IOError:
        print("unable to create file on disk.")

    finally:
        file.close()  #closes out the file = open(....)


if __name__ == '__main__':
    write_data("insertdata.txt", "This is my testing sample text") #don't need to already have a file of that name created, it will create a file with that name

#fine if you don't care about the earlier versions of your work
#if you mean to append data, then a different mode needs to be set

"""
Results

File was created, insertdata.txt
content

This is my testing sample text

"""