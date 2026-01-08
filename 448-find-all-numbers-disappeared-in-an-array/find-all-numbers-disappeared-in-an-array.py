class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)

        for i in range(n):
            while 1 <= nums[i] <= n and nums[nums[i] - 1] != nums[i]:
                c = nums[i] - 1
                nums[i], nums[c] = nums[c], nums[i]

        f = []
        for j in range(n):
            if nums[j] != j + 1:
                f.append(j + 1)

        return f

            

        