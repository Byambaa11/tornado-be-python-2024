fhand = open('mbox-short.txt')
for line in fhand:
    line = line.rstrip()
    splitted_line = line.split(' ')
    if line.startswith('From:'):
        print(line)
        