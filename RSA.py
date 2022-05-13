try:
   input = raw_input
except NameError:
   pass
try:
   chr = unichr
except NameError:
   pass
p=int(input('Enter prime p: '))
q=int(input('Enter prime q: '))
print("tiykargi sanlardi tanlan':\np=" + str(p) + ", q=" + str(q) + "\n")
n=p*q
print("n = p * q = " + str(n) + "\n")
phi=(p-1)*(q-1)
print("Eyler funktsiyasi (totient) [phi(n)]: " + str(phi) + "\n")
def gcd(a, b):
    while b != 0:
        c = a % b
        a = b
        b = c
    return a
def modinv(a, m):
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return None
def coprimes(a):
    l = []
    for x in range(2, a):
        if gcd(a, x) == 1 and modinv(x,phi) != None:
            l.append(x)
    for x in l:
        if x == modinv(x,phi):
            l.remove(x)
    return l
print("Tomendegi ko'p sonli massivden e ni tanlan':\n")
print(str(coprimes(phi)) + "\n")
e=int(input())
d=modinv(e,phi)
print("\nashiq giltiniz (e=" + str(e) + ", n=" + str(n) + ").\n")
print("\nSizdin uluma ashiq giltiniz(d=" + str(d) + ", n=" + str(n) + ").\n")
def encrypt_block(m):
    c = modinv(m**e, n)
    if c == None: print('No modular multiplicative inverse for block ' + str(m) + '.')
    return cv
def decrypt_block(c):
    m = modinv(c**d, n)
    if m == None: print('No modular multiplicative inverse for block ' + str(c) + '.')
    return m
def encrypt_string(s):
    return ''.join([chr(encrypt_block(ord(x))) for x in list(s)])
def decrypt_string(s):
    return ''.join([chr(decrypt_block(ord(x))) for x in list(s)])
s = input("Shifrlaw ushin xabardi kiritin: ")
print("\nOddiy xabar: " + s + "\n")
enc = encrypt_string(s)
print("Shifrlang'an xabar: " + enc + "\n")
dec = decrypt_string(enc)
print("DiShifrlang'an xabar: " + dec + "\n")