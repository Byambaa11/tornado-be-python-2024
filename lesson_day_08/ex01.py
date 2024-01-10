print('exercise 01')

a = [1,2,3]

def chop(list):
    print(list[0])
    print(list[-1])
    del list[0]
    del list[-1]
    return None


chop(a)
print(a)


a = [1,2,3]

def middle(list):
    print(list[0])
    print(list[-1])
    del list[0]
    del list[-1]
    return list


print(a)
b = [1,2,3,4,5,6]
middle(b)
print(b)

