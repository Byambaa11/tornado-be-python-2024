inp = input('enter fahrenheit temperature')
try: 
    fahr = float(inp)
    celcius = (fahr - 32.0) * 5.0 / 9.0
    print(celcius)
except:
    print('please enter a number')

    