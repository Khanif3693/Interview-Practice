 def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        n=len(nums)
        for i in range(n-1,-1,-1):
            if nums[i-1]<nums[i]:
                break
        if i==0:
            nums.sort()
        s,x=i,nums[i-1]
        for j in range(i+1,n):
            if nums[j]>x and nums[j]<nums[s]:
                s=j
        nums[s],nums[i-1]=nums[i-1],nums[s]
        nums[i:] = sorted(nums[i:] ) 
