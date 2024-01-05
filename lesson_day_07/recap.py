cheeses = ['Cheddar', 'Edam', 'Gouda', 12, 48.0, False,]
print(cheeses)
print(type(cheeses))


number = 0
while number < 10:
    number = number + 2
    # print(number)


# for i in cheeses:
    # print(i)

print(cheeses[3])
print(cheeses[5])
print(cheeses[-1])
cheeses[5] = True
print(cheeses)
cheeses[0] = 'life'
# print(cheeses)

t = ['a', 'b', 'c', 'd', 'e', 'f', ]
t[1:3] = ['x', 'y']
# print(t)

t = ['a', 'b', 'c', 'd', 'e', 'f', ]
t[:4]
print(t)



t1 = ['a', 'b', 'c']
t2 = ['d', 'e']
t1.extend(t2)
print(t1)

t = ['a', 'b', 'c']
t.append('d')
print(t)

t = ['d', 'c', 'e', 'b', 'a']
t.sort()
print(t)


t = ['a', 'b', 'c']
x = t.pop(1)
print(t)
print(x)


t = ['a', 'b', 'c']
del t[1]
print(t)


t = ['a', 'b', 'c']
t.remove('b')
print(t)


t = ['a', 'b', 'c', 'd', 'e', 'f']
del t[1:5]
print(t)


nums = [3, 41, 12, 9 ,74, 15]
print(len(nums))

print(max(nums))

print(min(nums))

print(sum(nums)/len(nums))



s = 'spam'
t = list(s)
print(t)


s = 'pining for the fjords'
t = s.split()
print(t)
print(t[2])


s = 'spam-spam-spam'
delimiter = '-'
s.split(delimiter)

a = 'banana'
b = 'banana'
a is b 
