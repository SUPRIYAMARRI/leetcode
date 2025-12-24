class Solution:
    def isPalindrome(self, x: int) -> bool:
        y=x
        s=0
        while(y>0):
            a=y%10
            s=10*s+a
            y=y//10
        if s!=x:
            return False
        else:
            return True


        