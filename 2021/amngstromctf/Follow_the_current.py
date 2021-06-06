import zlib
from itertools import product

Bytes=[chr(x).encode() for x in range(256)]
keys=list(product(Bytes, repeat=2))

def keystream(key):
    index = 0
    while 1:
        index+=1
        if index >= len(key):
            key += zlib.crc32(key).to_bytes(4,'big')
        yield key[index]



with open("/enc","rb") as f:
    cipher = f.read()
for key in keys:
	kk=b''
	for x in key:
	   kk+=x
	plain_text = b''
	k=keystream(kk)
	for i in cipher:
			plain_text+= chr(i ^ next(k)).encode()
	if b'actf{' in plain_text:
		print(plain_text)
		break
