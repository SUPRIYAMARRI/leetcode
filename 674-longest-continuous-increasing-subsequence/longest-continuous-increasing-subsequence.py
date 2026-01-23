class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        s=1
        f=1
        for i in range(1,len(nums)):
            if nums[i]>nums[i-1]:
                f+=1
            else:
                f=1
            s=max(s,f)
        return s
       




        