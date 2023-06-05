#dat file will end with 2 empty lines
#each poem starts with @ character

file = open('poems.dat', 'r')
lines = file.readlines()

print("[")
for i, line in enumerate(lines):
    previous=line if i==0 else lines[i-1]
    next=line if i==len(lines)-1 else lines[i+1]
    newline=chr(10)
    
    if line.startswith("@"):
    	print(f"""{{{newline}"title":"{line[1:][:-1]}",{newline}"lines":[""",end="")
    elif len(line) > 1:
        print(f""""{line[:-1]}""",end="\"")
        if len(next) > 1: print(",",end="")
    elif len(line) == 1 and not previous.startswith("@"):
    	print(f"]{newline}}}",end="")
    	if i<len(lines)-2: print(",\n",end="")
print("\n]")
