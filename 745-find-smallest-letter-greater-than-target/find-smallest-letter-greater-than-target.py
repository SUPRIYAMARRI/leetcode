class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        s=ord(letters[-1])
        b=0
        for i in letters:
            if ord(i)>ord(target):
                c=ord(i)
                s=min(s,c)
        if s<=ord(target):
            return letters[b]
        return chr(s)
       