  def twoSum(self, nums, target):
        from collections import defaultdict
        d=defaultdict(lambda:'a')
        if len(nums)<=1:
            return None
        for i,x in enumerate(nums):
            if d[target-x]=='a':
                d[x]=i
            else:
                return [d[target-x],i]
            
