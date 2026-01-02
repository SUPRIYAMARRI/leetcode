class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        b={}
        for i in range(len(nums)):
            if nums[i] not in b:
                b[nums[i]]=1
            else:
                b[nums[i]]+=1
        for j,count in b.items():
            if count==1:
                return j
            