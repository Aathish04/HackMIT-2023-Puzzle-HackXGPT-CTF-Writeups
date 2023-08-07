from pwn import *

#context.binary = '/home/aathishs/Desktop/hackvm/puzzle1'

commands = """
set logging enabled on
break *(0x800002f8)
ignore 1 10000
commands 1
continue
end
break *(0x80000324)
commands 2
info breakpoint 1
continue
end
continue

"""

context.arch = 'riscv32'
loweralphabet = list(string.ascii_lowercase)
upperalphabet = list(string.ascii_uppercase)
numbers = list(string.digits)
allchars = loweralphabet+upperalphabet+numbers+["_"]
print(string.printable)
#exit()
knownsizekey = "hack{aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa}"
with open("gdb.txt","w") as f:
	pass

# NOTE: THIS PROGRAM IS A LITTLE BUGGY - SINCE, ONCE THE LAST CHARACTER OF THE PASSPHRASE HAS BEEN DETERMINED
# THE BREAKPOINT IS HIT MORE THAN JUST FOR THE CHARACTER 

for i,c in enumerate(string.printable):
	init = "hack{in5tructi0n_s3ts_w4nt_t0_b3_fr33_18052010" # this was originally just the string 'hack{'. After each execution of this program, you can identify the character that has to be added to it one by one.
	mid = "#" * (len(knownsizekey)-len(init)-2)
	s = init+c+mid+"}"
	print(s)
	assert len(s) == len(knownsizekey)
	io = gdb.debug('/home/aathishs/Desktop/hackvm/puzzle1',commands)
	io.recv()
	io.sendline(s)
	with open("gdb.txt","r") as f:
		s = f.read()
		if f"breakpoint already hit {len(init)+1} times" in s:
			print("Found char: "+string.printable[i-1])
			break
with open("gdb.txt","r") as f:
	s = f.read()
	if f"breakpoint already hit {len(init)+1} times" in s:
		print("Found char: "+string.printable[i-1])
