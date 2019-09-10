def find(arry):
    result = []
    arry.sort()
    for target in arry:
        first = 0
        last = len(arry)-1
     
        while first < last:
         
            if arry[first] + arry[last] == target:
                result += [(arry[first],arry[last],target)]
                first+=1
                last-=1
            elif arry[first] + arry[last] < target:
               
                first +=1
            else:
                last -=1
              
    return result

if __name__ == "__main__":
    print (find([1, 4, 2, 3, 5]))
