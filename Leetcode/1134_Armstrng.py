class Solution(object):
    def isArmstrong(self, N):
        return N == sum([int(x)**len(str(N)) for x in list(str(N))])
        """
        :type N: int
        :rtype: bool
        """
        
