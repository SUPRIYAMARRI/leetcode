class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        a=bin(n)
        f=a[2:]
        for i in range(len(f)-1):
            if f[i+1]==f[i]:
                  return False
        return True




        