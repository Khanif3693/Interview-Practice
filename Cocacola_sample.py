#Hit compile and run to see a sample output.
#Read values from stdin, do NOT hard code input.

import fileinput
import sys
from collections import defaultdict
s=""
for line in fileinput.input():
    #sys.stdout.write(line)
    s=s+line
    
    
n,data=s.splitlines()
#print(int(n))
data=list(data.split(" "))
#print(data)
d=defaultdict(lambda:0)
for x in data:
    d[x]=d[x]+1
print( max(d.values()))
    

