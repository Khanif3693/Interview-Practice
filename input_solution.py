import fileinput
import sys
data=""
for line in fileinput.input("input.txt"):
    data=data+line


if not data=="":
    s,t= data.splitlines()
else:
     sys.exit()
s=s[2:]
t=t[2:]
print(s)
print(t)

for x in list(t.split()):
    print(x)
    if x in s:
        print("True")
    else:
        print("False")
        
