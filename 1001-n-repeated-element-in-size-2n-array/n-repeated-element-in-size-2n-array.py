class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        d={}
        for i in range(len(nums)):
            if nums[i] not in d:
                d[nums[i]]=1
            else:
                d[nums[i]]+=1
        for j,c in d.items():
            if c>1:
                return j
        