import random
import string
chars = string.punctuation + string.digits + string.ascii_letters + ' '
chars = list(chars)
key =  chars.copy()

##########INCRYPTION

random.shuffle(key)
plain_txt = input('Ente your text: ') 
cipher_txt = ''

for letter in plain_txt:
     index = chars.index(letter)
     cipher_txt += key[index]
print(cipher_txt)
     
##########DECRYPTION

cipher_txt = input('Enter ciphered text: ')
plain_txt = ''

for letter in cipher_txt:
     index = key.index(letter)
     plain_txt += chars[index]
print(plain_txt)

    