class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s=list(s)
        for  value in reversed(t):
            if s==[]:
                return True
            if value == s[-1]:
                s.pop()
        return not (len(s) > 0)
        
