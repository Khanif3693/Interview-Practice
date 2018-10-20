"""
This program takes input as string and return first character whose frequency is 1


for example:

"abcdabd" ==>  {'a': 2, 'c': 1, 'b': 2, 'd': 2} ==> So you can see that we have very first character is c whose frequency is 1.

let's take any other example: "abcd" ==>{'a': 1, 'c': 1, 'b': 1, 'd': 1} ==> it will print "a"
"""


def solution (str1): # input a string  --> output a character which contains only once 
    counts={}
    for x in str1:
        counts[x]=0
    for x in range(len(str1)):
        counts[str1[x]]=1+counts[str1[x]]
    print(counts)
    for x in str1:
        if(counts[x]==1):
            return x
        
    return 0
    
    
    
    
    
    
    
    
    
print(solution("abcdab")) #should print c
