print('Calculator')

operator = int(input('Give me operator: '))
print(operator)
operand = int(input('give me operand'))
print(operand)
operation = input('Give me operation')
print(operation)


    
try:
    if operation == "+":
        result = operand + operator
    elif operation == "-":
        result = operator - operand
    elif operation == "*":
        result = operator * operand
        print(result)
    elif operation == "%":
        result = operator % operand
        print(result)
    else:
        print('operation is not supperted')
except:
    print('give me number')
