class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        b={}
        for i in range(len(nums)):
            if nums[i] not in b:
                b[nums[i]]=1
            else:
                b[nums[i]]+=1
        for j,c in b.items():
            if c>=2:
                return True
        else:
            return False
        