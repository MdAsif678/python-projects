class Cipher:
    def __init__(self, message, key):
        self.message = message
        self.key = key
    
class CaesarCipher(Cipher):
    def __init__(self, message, key):
        super().__init__(message, key)

    
    def encrypt(self):
        encryptedmessage = ""
        for letters in self.message:
            if letters == " ":
                encryptedmessage += " "

            elif letters.islower():
                encryptedmessage += chr((ord(letters)-97 + self.key)%26+97)
            
            elif letters.isupper():
                encryptedmessage += chr((ord(letters)-65 + self.key)%26+65)
        
        return encryptedmessage
    
    def decrypt(self):
        decryptedmessage = ""
        for letters in self.message:
            if letters == " ":
                decryptedmessage += " "

            elif letters.islower():
                decryptedmessage += chr((ord(letters)-97 - self.key)%26+97)
            
            elif letters.isupper():
                decryptedmessage += chr((ord(letters)-65 - self.key)%26+65)
        
        return decryptedmessage
    
mess = CaesarCipher("Hey Homie how you doing gng",3)
print(mess.encrypt())

dmess = CaesarCipher("Khb Krplh krz brx grlqj jqj",3)
print(dmess.decrypt())