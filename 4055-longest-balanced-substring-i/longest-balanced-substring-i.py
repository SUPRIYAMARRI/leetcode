class Solution:
    def longestBalanced(self, s: str) -> int:
        m=0
        for i in range(len(s)):
            f={}
            for j in range(i,len(s)):
                if s[j] not in f:
                    f[s[j]]=1
                else:
                    f[s[j]]+=1
                v=f.values()
                if len(set(v))==1:
                    m=max(m,j-i+1)
        return m

