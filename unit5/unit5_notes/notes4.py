"""
example using example1.txt


"""

def read_file(fname):
    input_file = open(fname, "r")
    d={}


    for line in input_file:
        print("the lines:\t", line)
        fields = line.split(";") #split the data, which happens to be semi-colon deliminted
        d[fields[0]] = [["number_of_items", int(fields[1])],["price", float(fields[2])]]
        print(d)

    input_file.close()


if __name__ == "__main__":
    read_file("example1.txt")
