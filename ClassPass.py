#plese read classPass.txt for details of this program.

def solution(N,S):
    strng=S.split(" ") #Split given string
    avlbl=int(3*N) #Total seats 
    if(len(S) < 2):
        return avlbl #if given string is less than 2 it ll return total seats
    if(N==0):
        return 0
    listABC=[] #group of ABC
    listHJK=[] #group of HJK
    listEF=[]
    listD=[]
    listG=[]
    i=0
    print("rows",N, "Assigned ",strng)
    

    for x in range(N):
        listABC.append('FALSE')
        listHJK.append("FALSE")
        listEF.append("FALSE")
        listD.append("FALSE")
        listG.append("FALSE")
   
    for x in range(len(strng)):
        i=int(strng[x][0])-1
        

        if(not listABC[i]=="TRUE"):
            if(strng[x][1]=="A" or strng[x][1]=="B" or strng[x][1]=="C"):  #If any of ABC is seen that list set to true and seat -1
                avlbl=avlbl-1
                listABC[i]="TRUE"
        if(not listHJK[i]=="TRUE"):
            if(strng[x][1]=="H" or strng[x][1]=="J" or strng[x][1]=="K"):
                avlbl=avlbl-1
                listHJK[i]="TRUE"
        if(not listEF[i]=="TRUE"):
            if(strng[x][1]=="E" or strng[x][1]=="F"):
                avlbl=avlbl-1
                listEF[i]="TRUE"
        if(not listD[i]=="TRUE"):
            if(strng[x][1]=="D"):
                listD[i]="TRUE"
        if(not listG[i]=="TRUE"):
            if(strng[x][1]=="G"):
                listG[i]="TRUE"
        if(listG[i]=="TRUE" and listD[i]=="TRUE"):
            avlbl=avlbl-1
    

    return avlbl
            
                
        





print("Available",solution(3,"1A 2B 3C 2D"))
print("Available",solution(2,"1A 1F 1H 2G"))

print("Available",solution(2,"1A 2B 1C 2D"))
print("Available",solution(1,"1A 1F 1H"))
