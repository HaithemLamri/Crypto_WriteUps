from sage.all import *
from pwn import *
F=GF(691)
def printvect(v):
    return "".join(chr(x) for x in v[::-1])


conn = remote('crypto.2021.chall.actf.co', 21601)
conn.recvline()
for l in range (29,50):

    v=[]
    M=Matrix(F,[[((x+1) **i) %691 for i in range(l)] for x in range(l)])
    for p in range(1,l+1):
        conn.send(str(p) +'\n')
        v.append(int(conn.recvuntil('\n').decode()[5:]))
    V=vector(F,v)
    if "actf{" in printvect(M.solve_right(V)) :
        print(printvect(M.solve_right(V)))
        break









