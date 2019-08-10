class Solution(object):
    def reorderLogFiles(self, logs):
        a=logs
        letter=[]
        digit=[]
        for x in a:
            space=x.find(" ")
            id=x[:space]
            logs=x[space+1:]
            if (logs.replace(" ","")).isdigit()==True:
                digit.append(x)
            else:
                letter.append(logs+" "+ id)
       
        res=[]
        for x in sorted(letter):
            space=x.rfind(" ")
            res.append(x[space+1:]+" " +x[:space])
            
        res=res+digit
        return res
    
        """
        :type logs: List[str]
        :rtype: List[str]
        """
        
