class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        b={}
        for i in range(len(nums)):
            if nums[i] not in b:
                b[nums[i]]=1
            else:
                b[nums[i]]+=1
        for j,c in b.items():
            if c > len(nums)//2:
                return j
            
                

        