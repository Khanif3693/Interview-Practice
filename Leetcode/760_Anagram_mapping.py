def anagramMappings(self, A, B):
        res=[]
        for x in A:
            res.append(B.index(x))
        return res
