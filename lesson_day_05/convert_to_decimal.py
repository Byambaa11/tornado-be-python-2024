binary=int(input('enter number'))
rest=0
power=0
while binary>0:
    if binary % 10 **(power + 1) != 0:
        rest=rest + 2 ** power
        binary = binary - 10 ** power
        
    power = power + 1
    
print(rest)


def convert_to_bin(input):
    rest = 0
    power = 0
    while input > 0:
        if input % 10**(power + 1) != 0:
            
