# __author__ Saurabh
# Stanford University
# Cryptography I
# https://www.coursera.org/course/crypto

# Week 1
# Question 1
# Many Time Pad 

# Let us see what goes wrong when a stream cipher key is used more than once. Below are eleven hex-encoded ciphertexts that are the result of encrypting eleven plaintexts with a stream cipher, all with the same stream cipher key. Your goal is to decrypt the last ciphertext, and submit the secret message within it as solution. 
# Hint: XOR the ciphertexts together, and consider what happens when a space is XORed with a character in [a-zA-Z]. 
import codecs
import string
with open("ciphertext.txt", "r") as cphr:
    cipher_text = []
    for line in cphr:
        cipher_text.append(codecs.decode(line.strip(),'hex'))

def strxor(a, b):     # xor two strings of different lengths
    if len(a) > len(b):
       return "".join([chr(ord(x) ^ ord(y)) for (x, y) in zip(a[:len(b)], b)])
    else:
       return "".join([chr(ord(x) ^ ord(y)) for (x, y) in zip(a, b[:len(a)])])


def decrypt(key, msg):
    c = strxor(key, msg)
    return c

target_msg = 'The secret message is: When using a stream cipher, never use the key more than once'

if __name__=='__main__':
    for i in range(10):
        decrypt_msg = decrypt(cipher_text[10],cipher_text[i])
        print("guesing :-",i),
        for j in range(len(cipher_text[10])):
             if ord(decrypt_msg[j]) in range(41,122):
                print(decrypt_msg[j]),
             else:
                print("."),

        print(".........END")
    
    key = decrypt(target_msg,cipher_text[10])
    print("KEY : ", key)
    for i in range(11):
        msg = decrypt(key,cipher_text[i])
        print("massege : ",i,msg)
