class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        c=[]
        for i in nums:
            if i not in c:
                c.append(i)
        c.sort()
        if len(c)<3:
            return c[-1]
        else:
            return c[-3]

        


        