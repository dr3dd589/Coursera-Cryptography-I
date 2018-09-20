import codecs

def xor_strings(a,b):
    enc = "".join(chr( ord(c) ^ ord(d) ) for (c,d) in zip(a,b))
    return enc

msg1 = "attack at dawn"
enc1 = codecs.decode("6c73d5240a948c86981bc294814d",'hex')
key  = xor_strings(msg1,enc1)

msg2 = "attack at dusk"
print(codecs.encode(xor_strings(msg2,key),'hex'))