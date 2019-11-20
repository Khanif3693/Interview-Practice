from copy import deepcopy
def fun (grid, k, rules):
    
    if not grid:
        return grid
    rows=len(grid)
    cols=len(grid[0])
    print(rows,cols)
    
    i=1
    tmp=deepcopy(grid)
    print(tmp,"tmp first print")
    while( i < k):
        for x in range(rows):
            for y in range(cols):
                print(x,y)
                count=0
                count+=1 if x-1 >=0  and y-1 >=0 and  grid[x-1][y-1]==1 else 0
                print("1",count)
                count+=1 if x-1 >=0  and  grid[x-1][y]==1 else 0
                print("2",count)
                count+=1 if x-1 >=0  and y+1 < cols and  grid[x-1][y+1]==1 else 0
                print("3",count)
                count+=1 if y-1 >=0 and  grid[x][y-1]==1 else 0
                print("4",count)
                count+=1 if y+1 < cols and  grid[x][y+1]==1 else 0
                print("5",count)
                count+=1 if x+1 < rows  and y-1 >=0 and  grid[x+1][y-1]==1 else 0
                print("6",count)
                count+=1 if x+1 < rows  and  grid[x+1][y]==1 else 0
                print("7",count)
                count+=1 if x+1 < rows  and y+1 < cols and  grid[x+1][y+1]==1 else 0
        
            
            
                print(count)    
                if rules[count]=="alive":
                    print("tmp is alive")
                    tmp[x][y]=1
                else:
                    tmp[x][y]=0
            
        grid=deepcopy(tmp)    
        i+=1
        print("iteration")
        for x in grid:
            print(x)
            
    print(grid)               
                    
    
grid=[
    [0,1,0,0],
    [0,0,0,0]
    ]
k=3
rules=["dead","alive","dead","dead","dead","alive","dead","dead","dead"]
print(fun(grid, k, rules))
