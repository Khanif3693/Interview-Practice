def findMaxCommonality(stri):
    count = [0 for _ in range(26)]
    for i in stri:
        count[ord(i) - 97] += 1

    res = 0
    cur = 0
    for i in stri:
        print("before",cur,res)
        print("now reading ", i)
        
        if count[ord(i) - 97] > 1:
            cur += 1
            count[ord(i) - 97] -= 2
        elif count[ord(i) - 97] == 0:
            cur -= 1
        else:
            count[ord(i)-97]-=1
        res = max(cur, res);
        print("After",cur,res)
    return res

print (findMaxCommonality('abcdecdaaaaaa'))
