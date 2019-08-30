class Solution(object):
    def letterCombinations(self, digits):
        
        if not digits or '0' in digits or '1' in digits:
            return []
        res=[[]]
        
        dic={'2':['a','b','c'],
             '3':['d','e','f'],
             '4':['g','h','i'],
             '5':['j','k','l'],
             '6':['m','n','o'],
             '7':['p','q','r','s'],
             '8':['t','u','v'],
             '9':['w','x','y','z']
            }
        for digit in digits:
            tmp=[]
            for x in res:
                for l in dic[digit]:
                    tmp.append(x+[l])
                    
            res=tmp
            
        return ["".join(x) for x in res]
        """
        :type digits: str
        :rtype: List[str]
        """
        
