class Solution(object):
    def countSubstrings(self, s):
        def searchPalindrome(left, right):
            count = 0
            while left >= 0 and right < len(s) and s[left] == s[right]:
                count += 1
                left -= 1
                right += 1
            return count
        
         

        res = 0
        for i in range(len(s)):
            res += searchPalindrome(i, i)
            if i+1 < len(s):
                res += searchPalindrome(i, i+1)
        return res
        """
        :type s: str
        :rtype: int
        """
        
