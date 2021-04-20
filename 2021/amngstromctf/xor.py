
from pwn import *
msg1="ae27eb3a148c3cf031079921ea3315cd27eb7d02882bf724169921eb3a469920e07d0b883bf63c018869a5090e8868e331078a68ec2e468c2bf13b1d9a20ea0208882de12e398c2df60211852deb021f823dda35079b2dda25099f35ab7d218227e17d0a982bee7d098368f13503cd27f135039f68e62f1f9d3cea7c"
msg= unhex(msg1)
print(msg)
from  Crypto.Util.number import bytes_to_long
import  pandas as pd
import  xortool.tool_main






def XoR(a,b):
    ret = b''
    for i in range(0,len(a),5):
         ret += xor(a[i:i+5],b)
    return ret







keys=[]
fl=xor(msg,b'actf{')
for j in range(len(fl)-5):
 for i in range(0,len(fl),5):
    keys.append(fl[i+j:i+5])


def sol(cipher,keys):

    for key in keys:
        if b'actf{' in XoR(cipher,key):
            print(f"----flag = {XoR(cipher,key)}")
            print(key)


sol(msg,keys)


















