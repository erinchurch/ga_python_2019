

def read_file(fname1, fname2):
    data_file = open(fname1, "r")
    header_file = open(fname2, "r")

    header = []
    d_temp = {}
    d_t = {}
    d_input = {}
    g = {}

    for line in header_file:
        print(line)
        header = line.split(";")


    for line in data_file:
        field = line.split(";")
        field.pop()
        for i in range(len(field)):
            d_t = {}
            g[header[i]]=field[i]
            d_t.update(g)
            d_temp[field[0]]=d_t
            d_input.update(d_temp)
    return(d_input)



if __name__ == "__main__":
    read_file("accounts.txt", "headers_accounts.txt")