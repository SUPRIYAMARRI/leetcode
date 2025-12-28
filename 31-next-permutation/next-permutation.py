class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)

        # STEP 1: find first index i from right such that nums[i] < nums[i+1]
        i = n - 2
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1

        # STEP 2: if no such index found, array is in descending order
        if i == -1:
            nums.reverse()
            return

        # STEP 3: find index j from right such that nums[j] > nums[i]
        j = n - 1
        while nums[j] <= nums[i]:
            j -= 1

        # STEP 4: swap nums[i] and nums[j]
        nums[i], nums[j] = nums[j], nums[i]

        # STEP 5: reverse the part after index i
        nums[i + 1:] = reversed(nums[i + 1:])


        