def make(filename):
    f = open(filename, 'r')
    output = []
    for line in f:
        substring = line[1:-2]
        temp = substring.split(", ")
        output.append(temp)
    f.close()
    return output