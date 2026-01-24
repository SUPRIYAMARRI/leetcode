class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        s=[]
        L=0
        r=len(nums)-1
        while L<r:
            b=nums[L]+nums[r]
            s.append(b)
            L+=1
            r-=1
        return max(s)


        