class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        s=0
        f=0
        for i in nums:
            s+=i
        for j in range(len(nums)+1):
            f+=j
        return f-s




        