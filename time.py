#Please read the time.txt for the details

def solution(S):
    S = S.replace(":", "")
    ls = []

    gt = int(S)
    if (S[0] == S[1] == S[2] == S[3]):
        return S[0] + S[1] + ":" + S[2] + S[3]
    for i in range(len(S)):
        for j in range(len(S)):
            for k in range(len(S)):
                for l in range(len(S)):
                    if (int(S[i] + S[j] + S[k] + S[l]) < gt):
                        ls.append(S[i] + S[j] + S[k] + S[l])

    S = max(ls)
    return S[0] + S[1] + ":" + S[2] + S[3]


print(solution("22:22"))
print(solution("22:21"))
print(solution("21:22"))
print(solution("10:00"))

