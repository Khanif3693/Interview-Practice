def fun(x, Y, mat):
    dp=[[float("+inf") for rows in range(x+1)] for y in range(Y+1)] 
    print(dp)
    if mat[0][0]==0:
        return -1
    else:
        dp[1][1]=1
        
        return bfs(mat, dp)
                    

def bfs(mat, dp):
   
    for x,data in  enumerate(mat) :
        for y,elem in enumerate(data):
           
            if mat[x][y]==1 and dp[x+1][y+1]==float("+inf"):
                
                dp[x+1][y+1]=min(dp[x][y+1],dp[x+1][y])+1
            elif mat[x][y]==0:
                    continue
            elif mat[x][y]==9:
                x= min(dp[x][y+1],dp[x+1][y])
                if x==float("+inf"):
                    return -1
                else:
                    return x
                
            else:
                continue
                
                
                
            
                
                    
           
    
    
    
            
    
    
    
    
    
    
    


rows=5
cols=4
mat=[
    [1,1,1,1],
    [0,1,1,1],
    [0,1,0,1],
    [1,1,9,1],
    [0,0,1,1]
    ]
    
mat=[[1,0,0],
[1,1,0],
[1,9,0]]

    

print(fun(3,3, mat))
    
    
    
