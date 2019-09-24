class Solution(object):
    def climbStairs(self, n):
        dp=[1,1]
        last=0
        last1=1
        for x in range(n):
            dp.append(dp[last]+dp[last1])
            last1+=1
            last+=1
        return dp[n]
            
        
        """
        :type n: int
        :rtype: int
        """
        
