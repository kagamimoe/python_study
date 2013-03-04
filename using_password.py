#kaisa password

def encrypt_one(str):
    if ord(str) in range(65,122):
        str = chr(ord(str)+2)
    return str

def encrypt(str):
    return map(encrypt_one,str)
    
print ''.join(encrypt('abcdefg'))
