fname = input('Enter the file name: ')

try:
     fhand = open(fname)
except:
    print('File cannot be opened')
    exit()
count = 0
for line in fhand:
    if line.startswith('Subject:'):
     count = count + 1
    print('There were', count, 'subject lines in', fname)
    
    if   fname==input('Enter the file name:na na boo boo '):
       print("na na boo boo to you - you have been punk' d ")
       
           