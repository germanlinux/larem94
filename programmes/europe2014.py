import sys
file = sys.argv[1]
with open(file, 'r', encoding='iso-8859-1') as infile:
    for line in infile:
        if line[:5] == '1;94;'  :
            line = line[:-1]
            print(line)
