class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        k=0
        m=0
        for i in s:
            k+=ord(i)
        for j in t:
            m+=ord(j)
        g=m-k
        return chr(g)

