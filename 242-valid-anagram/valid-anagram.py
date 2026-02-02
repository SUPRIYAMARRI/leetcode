class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        b=sorted(s)
        c=sorted(t)
        if b==c:
            return True
        return False
        