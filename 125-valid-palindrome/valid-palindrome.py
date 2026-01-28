class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=s.lower()
        b=""
        for i in s:
            if i.isalnum():
                b+=i
        a=b[::-1]
        if b==a:
            return True
        elif a==" ":
            return True
        else:
            return False
        