def convert_to_binary(number):
    rest = 0
    while  number > 0:
        rest = number % 2
        number = number // 2
        print(rest)
    
convert_to_binary(4)
    