n = 5
# while n > 0:
#     print(n)
#     n = n - 1
# print('blastoff')
    
    
# while True:
#     line = input('>')
#     if line == 'done':
#         break
#     print(line)
# print('The end!')


# while True:
#     line = input('>')
#     if line[0] == '#':
#         continue
#     if line == 'done':
#         break
#     print(line)
# print('The end!')


start = 15
end = 25
sum = 0
while start <= end:
    sum = sum + start
    start = start + 1
print(sum)

    
    
n = 10
while n > 0:
    print("hello world", n)
    n = n -1
    
    
start = 1
end = 10
sum = 1
while start <= end:
    sum = sum * start
    start = start + 1
print(sum)



friends = ['joseph', 'Glenn', 'Sally']
for friend in friends:
    print('happy new year:', friend)
print('done!')


count = 0
for element in [3, 41, 12, 9, 74, 15]:
    count = count + 1
print('count:', count)



largest = None
print('before:', largest)
for element in [3, 41,12, 9, 74, 15]:
    if largest is None or element > largest:
        largest = element
    print('Loop :', largest)
print('largest:', largest)


smallest = None
print('before:', smallest)
for element in [3,41, 12, 9, 74, 15]:
    if smallest is None or element < smallest:
        smallest = element
    print('Loop:', element, smallest)
print('smallest:', smallest)


