def parse_value(string):
    string = string.strip()
    try:
        n = float(string)
    except ValueError:
        return string
    if '.' in string:  
        return n
    else:
        return int(n)


def parse_line(line):
    elements = line.split(',') 
    return [parse_value(x) for x in elements]


def parse_csv(path):
    with open(path,"r") as file_reader:
        whole_csv = []
        for line in file_reader:
            whole_csv.append(parse_line(line))
    return whole_csv

   