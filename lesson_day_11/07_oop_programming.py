class Father:
    def __init__(self, name, age, nationality):
        self.name = name 
        self.age = age 
        self.nationality = nationality
        
    def say_hello(self):
        print(f'Hello, my name is {self.name}, i am {self.age} years old, i have nationality {self.nationality}')
    
class Son(Father):
    def greeting(self):
        print('Hello, I am son')

class daughter (Father):
    def greeting(self):
        print('Hello, I am daughter')
        
uvgunkhuu = Father('Uvgunkhuu', 67, 'Mongolian')
uvgunkhuu.say_hello()
khangaikhuu = Son('Khangaikhuu', 18, 'Mongolian')
khangaikhuu.say_hello()
khangaikhuu.greeting()
marta = daughter('Marta', 20, 'Mongolian')
marta.say_hello()
marta.greeting()

        