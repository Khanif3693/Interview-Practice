   def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        paragraph = paragraph.replace("!"," ")
        paragraph = paragraph.replace("?"," ")
        paragraph = paragraph.replace("'"," ")
        paragraph = paragraph.replace(","," ")
        paragraph = paragraph.replace(";"," ")
        paragraph = paragraph.replace("."," ")
        
        d = defaultdict(lambda:0)
        paragraph = paragraph.lower()
        paragraph = paragraph.split(" ")
        for i in paragraph:
            if(i not in banned and i!=""):
                d[i] += 1
        v = max(d.values())
        print(d)
        l = []
        for key,value in d.items():
            if(value == v):
                l.append(key)
        del d
        return l[0]
