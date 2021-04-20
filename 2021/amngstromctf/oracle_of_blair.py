from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from  Crypto.Util.number import bytes_to_long
import os
from pwn import xor,unhex,enhex,remote
key = os.urandom(32)

padd=(b'\x08')*39
print(enhex(padd))
pd=(b'\x08')*16
"""
conn = remote('crypto.2021.chall.actf.co', 21112)
for i in range(16):
 conn.recvuntil(b':')
 print(i)
 conn.send(enhex(b'{}')+i*enhex(b'a') +'\n')
 s=conn.recvuntil(b'\n')
 print(len(s))

"""
"""
while 1:
    try:
        i = bytes.fromhex(input("give input: "))
        if not i:
            break
    except:
        break
    iv = os.urandom(16)
    inp = i.replace(b"{}", flag)

    if len(inp) % 16:
        inp = pad(inp, 16)
    print(inp)
    print(
        AES.new(key, AES.MODE_CBC, iv=iv).decrypt(inp).hex()
    )
"""
pl="5d6c3808943beca01855255058b7ba5323efd79393f9362d8ee6b1ad7efee04bef47e5051e1252fbcc761ab1f89c26858c2ab26875780590b9761ab1f89c2685"
pl=unhex(pl)
print(len(pl))
flag2=xor(pl[32:48],pl[48:64])
flag2=xor(flag2,pd)
print(enhex(flag2))
print(flag2)

flg="df887754ffb551053dddbd26d88667ff69d3d00ebe981d568621c8fea173d97863d5fb0da6992056a444af84cc24bd19"
flg=unhex(flg)
print(len(flg))
print(xor(xor(flg[16:32],xor(flg[32:])),flag2))

secr='actf{cbc_more_like_ecb_c}'

