class Solution(object):
    def findJudge(self, n, trust):
        if n == 1 and len(trust) == 0:
            return 1

        trustList = [0] * (n+1)

        for t in trust:
            trustList[t[0]] -= 1
            trustList[t[1]] += 1

        if (n-1) in trustList:
            return trustList.index(n-1)
        return -1