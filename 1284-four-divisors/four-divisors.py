class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        s=[]
        for i in nums:
            c=[]
            for j in range(1,int(i**0.5)+1):
                if i%j==0:
                    c.append(j)
                    if j!=i//j:
                        c.append(i//j)
                if len(c)>4:
                    break
            if len(c)==4:
                a=sum(c)
                s.append(a)
        b=0
        for m in s:
            b+=m
        return b

                



        