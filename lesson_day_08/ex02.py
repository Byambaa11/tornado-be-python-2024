unique_words = []

try:
    fhand = open('romeo.txt')
except:
    print('file cannot be opened:', 'romeo.txt')
    exit()
    
count = 0
for line in fhand:
    line = line.rstrip()
    splitted_line = line.split(' ')
    for w in splitted_line:
        if w not in unique_words:
            unique_words.append(w)
print(unique_words)
unique_words.sort()
print(unique_words)
print('There were', count, 'subject lines in', 'romeo.txt')



    
                       