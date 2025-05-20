def generate_key():
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    res = []
    for i in range(13):
        if((i&1)==0):
            s = ord(alphabet[i]) + i * 2
        else:
            s = ord(alphabet[i]) - i * 3
        res.append(chr((s%26) + ord('a')))
    return ''.join(res)

def rotR(x, shift):
    return ((x >> shift) | ((x << (8-shift) & 0xFF))) & 0xFF

def shuffle(ch,pin):
    ch = list(ch)
    n = len(ch)
    for i in range(0,n-1):
        j = (pin + i) % n
        ch[i], ch[j] = ch[j], ch[i]
    return ''.join(ch)

def str_deobfuscate(ch, shift):
    ch = list(ch)
    dec = []
    for x in ch:
        x = rotR(x,shift)
        dec.append(chr(x & 0xFF))
    return ''.join(dec)

def decrypt(ch, key):
    key_length = len(key)
    result = ''.join(chr(ch[i] ^ ord(key[i % key_length])) for i in range(len(ch)))
    return result

enc = "5cd447c055c1c4ddd7cc51ce405ad243c1cdc9c853c55dd4dd43dc5dc64bdbca4a787077d872"
dec = bytes.fromhex(enc)
key = generate_key()
pin = 0xcafe
key = shuffle(key,pin)
c_decrypt = decrypt(dec,key)
c_decrypt = c_decrypt.encode()
flag = str_deobfuscate(c_decrypt,7)
print(flag)
