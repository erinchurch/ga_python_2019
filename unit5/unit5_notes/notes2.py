


def read_data(file_name):
    file = open(file_name, 'r')
    try:
        for line in file:
            print(line)
    except FileNotFoundError:
        print(file_name, 'is not exists')
    finally:
        file.close()


if __name__ == '__main__':
    read_data('data1.txt')

"""

read_file('data.txt')

results

erin learning about files and pulling them in

yay!

line 3

line 4

line 5

happy passover

Process finished with exit code 0

"""

"""
file name change doesn't work 

the try/catch doesnt work 
"""