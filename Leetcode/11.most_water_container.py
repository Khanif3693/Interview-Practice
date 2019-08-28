def maxArea( height):
    start = 0
    end = len(height) - 1
    ans = 0
    
    while start < end:
        
        area = (end - start) * min(height[start], height[end])
        if area > ans:
            ans = area
        if height[start] > height[end]:
            end -= 1
        else:
            start +=1
        #print(area)
    return ans
        
        
        
print(maxArea([1,8,6,2,5,4,8,3,7]))
