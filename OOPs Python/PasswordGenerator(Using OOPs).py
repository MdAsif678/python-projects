import random
import string

class PasswordGenerator:
    def __init__(self, length, use_special, use_numbers):
        self.length = length
        self.use_special = use_special
        self.use_numbers = use_numbers

    def generate(self):
        pool = string.ascii_letters
        sp_char = string.punctuation
        num = string.digits

        if self.use_special == True:
            pool += sp_char
        
        if self.use_numbers == True:
            pool += num

        passw = ""
        for _ in range(self.length):
            passw += random.choice(pool)
        
        return passw

pass1 = PasswordGenerator(8,True,True)
pass2 = PasswordGenerator(8,False,True)
pass3 = PasswordGenerator(8,True,False)
pass4 = PasswordGenerator(8,False,False)

print(pass1.generate())
print(pass2.generate())
print(pass3.generate())
print(pass4.generate())