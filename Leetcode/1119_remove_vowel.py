 def removeVowels(self, S):
   hashset = {'a','e','i','o','u'}
        for char in S:
            if char in hashset:
                S = S.replace(char, "")
        return S
       
       
      
