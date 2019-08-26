class Solution(object):
    def sumOfDigits(self, A):
        a=min(A)
        res=0
        for x in str(a):
            res=res+int(x)
        return 1 if res%2==0 else 0
        
        """
        :type A: List[int]
        :rtype: int
        """
        
