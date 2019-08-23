 def removeVowels(self, S):
        vowels=['a','e','i','o','u']
        res=""
        for x in S:
            if x in vowels:
                continue
            else:
                res=res+x
        return res
