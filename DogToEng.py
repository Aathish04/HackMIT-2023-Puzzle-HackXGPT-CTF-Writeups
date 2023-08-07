Sentence1 = "Oh No!"
Sentence2 = "Rurl the Retriever flew up, up, and away and stumbled upon HackXAI's headquarters."
Sentence3 = "In order to make it back in time for HackMIT's 10th birthday, you need to help Rurl solve a series of challenging puzzles."
Sentence4 = "If you accept this challenge, enter Rurl's passphrase!"
s = """wOofWooF wOOfwOOf woOfwoof wOOFWooF wOOfWOOF wOOFwOoF woOfwoof wOOfwooF wOOfwoOF wOOfwoOF wOOfwOoF wOOFwoof wOOFwOof woOfwoof wOOFwOof wOOfWoof wOOfWooF wOOFwoOF woOfwoof wOOfwoOF wOOfWoof wOOfwooF wOOfWOof wOOfWOof wOOfwOoF wOOfWOOf wOOfwOOF wOOfwOoF woOfWOof woOfwoof wOOfwOoF wOOfWOOf wOOFwOof wOOfwOoF wOOFwoOf woOfwoof wOoFwoOf wOOFwOoF wOOFwoOf wOOfWOof woOfwOOF wOOFwoOF woOfwoof wOOFwoof wOOfwooF wOOFwoOF wOOFwoOF wOOFwoof wOOfWoof wOOFwoOf wOOfwooF wOOFwoOF wOOfwOoF woOfwooF """
b = ""
for c in s:
    if c.isupper():
            b+="1"
    elif c.islower():
            b+="0"
    else:
            b+=" "

b = "".join([chr(int(c,2)) for c in b.split()])

print(b)