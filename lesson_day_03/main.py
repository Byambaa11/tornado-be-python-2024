print('Calculator')

operator = int(input('Give me operator: '))
print(operator)
operand = int(input('give me operand'))
print(operand)
operation = input('Give me operation')
print(operation)

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

    
