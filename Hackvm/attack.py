from pwn import *

context.arch = "riscv32"

knownsizekey = "hack{aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa}" # from reading disasm of code we know size == 48

gdb_log_file = "gdb.txt"

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


with open(gdb_log_file,"w") as f:
    pass

def generate_test_key(init,c):
    s = init + c + ("#" * (len(knownsizekey)-len(init)-2)) + "}"
    assert len(s) == len(knownsizekey)
    return s

init = "hack{"
num_chars_to_fill = len(knownsizekey) - len(init) - 1

print(num_chars_to_fill)
for _ in range(num_chars_to_fill):
    for c in string.printable:
        s = generate_test_key(init,c)
        print(s)
        io = gdb.debug('/home/aathishs/Desktop/hackvm/puzzle1',commands,api=True)
        io.recv()
        io.sendline(s)
        io.recv()
        io.gdb.quit()
        with open(gdb_log_file,"r") as f:
            contents = f.read()
        num_occurrences = re.findall(r"breakpoint already hit (\d*) times",contents,re.M|re.DOTALL)
        num_occurrences = [int(j) for j in num_occurrences]
        if any( [j>len(init) for j in num_occurrences]):
            print(f"Passwd so far: {s}") 
            init  = init+c
            break
