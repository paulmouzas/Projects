# Caesar key

def encrypt(code, key):
    return ''.join(map(lambda x: chr(ord(x)+key), code))
   
def decrypt(code, key):
    return ''.join(map(lambda x: chr(ord(x)-key), code))
