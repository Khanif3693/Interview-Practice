  def calculateTime(self, keyboard, word):
        indx={}
        for i, x in enumerate(keyboard):
            indx[x]=i
            
        move=0
        curr=0
        for l in word:
            move+=abs(indx[l]-curr)
            curr=indx[l]
        return move
