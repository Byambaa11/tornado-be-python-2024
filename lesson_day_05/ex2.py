fname = input('Enter the file name: ')
fhand = open(fname)
count = 0
sum = 0
for line in fhand:
    if line.startswith('X-DSPAM-Confidence:'):
        count += 1
        sum += float(line[-7:])
       
        
print(count)
print(sum)

print(sum / count)
