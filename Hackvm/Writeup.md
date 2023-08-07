# HackVM

tl;dr: The usage of memcmp() when comparing the input password with the actual password could be used to develop a side-channel timing attack, since memcmp() will take longer to process more correct characters in the input password.

Note: I _probably_ didn't solve this challenge the intended way, (using timing), but I did follow the intended solution "category" which is Side-Channel "Timing" analysis.

## The Briefing

> As nature's engineers, beavers love all things (reverse) engineering, including reduced instruction set computers! Now the beavers by your local dam are excited to show you their [new RISC virtual machine & reversing challenge!](https://hackvm.hackxgpt.com/u/Aathish04_00aa27)

Clicking the link takes us to [this site:](https://hackvm.hackxgpt.com/)

[Briefing Page](./images/Briefing.png)

## Stage 1 - Reconnaissance

From the hints, we see that we've been given a sort of "template" for the passphrase. We've also been directed to find out why using `memcmp` could be harmful. Looking at `memcmp`'s `man`-page:

[Why no memcmp](./images/WhyNoMemcmp.png)

So it seems like we'll have to leverage the fact that we can identify how correct a particular passphrase is from just the time taken.

Let's try and figure out as much as we can about the `puzzle1` and `vm` binaries.

Running `file` on the binaries tells us that the `vm` binary is an `x86-64` executable and that the `puzzle1` binary is a `RISCV32` executable. Neither binary is stripped, and both are statically linked.

Running `strings` on the `puzzle1` binary reveals that while there's no cleartext password stored, there's a `.crypto` section in the assembly somewhere along with a `ciphertext` passphrase, so perhaps the program is hashing our input passphrase and comparing it with the ciphertext?

Trying to dump the assembly of the files, I face my first hurdle - I'm running `Kali ARM64`, so `objdump` can't easily dump the assembly of `RISCV` or `x86-64` architectures. I'm sure I could fix this somehow, but might as well use this as an opportunity to learn `ghidra`!

We initialise `ghidra`, make a new project, drag our `puzzle1` executable inside, and start the `CodeBrowser`:

[Ghidra First Look](./images/GhidraFirstLook.png)

After hitting `analyse` on the code, we are dropped into what `ghidra` says is the `main()` function, and can see the disassembly of the code to our left, and the decompiled `C` code to our right.

It's important to never trust the `C` that `ghidra` outputs blindly. Here, we simply observe that the program initialises a couple of variables, prints a message, reads a string, and first compares the length of that string to a value, and if that checks out, performs a `memcmp` with the string and some other `password` ciphertext. If `memcmp` says there's no difference, then the `win` function is called, which presumably prints the flag after reading it from a file.

Let's look at what the `memcmp` does:


[Ghidra `memcmp`](./images/GhidraMemcmp.png)

Right. This seems to be a little more complex than a standard `memcmp` function but not too different.

The function takes the two byte-arrays for comparison, and the number of characters to compare.

If the number of characters to compare is not zero, it hashes a portion of the first byte array, and compares it with a portion of the second byte array. It seems like this implementation of `memcmp` also implements the hashing of the first (input password) byte array instead of outsourcing it to it's own function.

All the same, the important parts are at line 31 and 32 of the decompiled C, and memory address `0x800002ec` of the disassembly. 

[Important `asm` and `C` code](./images/ImportantASMC.png)

If at any point during the execution, the current characters being compared from the input string and the `hash`ed password don't match, then the function returns. This means `memcmp` will take more time to check a password in which you got the first "x" characters right than it will to check a password where you didn't get the first "x" characters correct.


## Stage 2 - A Side Channel Timing Attack

I tried running a timing analysis by using a Jupyter Notebook in Google Colab to [generate](./Generate.ipynb) all possible combinations of the first few characters after `hack{`, and wrote also [code to use this list](./Attack.ipynb) to check the time taken to process the password. Ideally, this would consistently report that the password with the correct beginning took more time to process than the others.

Unfortunately, I just couldn't get consistent timing results. One one run, it would report that one string was the right one to begin with, and on others, it would report that other strings took longer to process.

I strongly suspect this had to do with my computer's cache just making the processing time for subsequent trials shorter, and the fact that I was running a `RISCV32` binary through an x86-64 VM executable through `Rosetta` in a Linux VM on a Mac. Maybe there were too many layers of abstraction to help get consistent results?

I then tried using `QEMU` (an emulator), rather than `Rosetta`  (a translation layer) to run the `vm` executable to get consistent results, but that didn't seem to work either.

I then tried running the `puzzle1` executable through `QEMU` directly, which worked like a charm!

I could try running a timing analysis here, but since `QEMU` offers support for debugging executables via `gdb`, I might as well try using the exact number of times the comparision loop runs as a cue to find which character was the correct character in the password - the correct character would take one more iteration of the loop to process than the fake ones.

I used `pwntools` to start a debug session on the `puzzle1` executable, and wrote some `gdb` commands to set breakpoints a the _incrementing_ portion of the loop, and at the conditional statement before the return. In order to count the number of times the loop is run, I can simply count the number of times the breakpoint for the incrementing portion is hit.

I'm sure there's a way to get the `gdb` debug log directly as a string, but instead, I made it write to a log file. The log file will contain the details of the debug session, and from there I can read off how many iterations the loop went through. The character for which the loop traverses one more time than usual is the next correct character of the passphrase.

[Program Running](./images/Running.png)

Slowly but surely, character by character, the final passphrase is built, and I can enter it in the webshell version of the challenge to get the flag!