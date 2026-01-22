from typing import List

class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        operations = 0

        # Repeat until array becomes non-decreasing
        while True:

            # 1️⃣ Check if array is non-decreasing
            is_non_decreasing = True
            for i in range(1, len(nums)):
                if nums[i] < nums[i - 1]:
                    is_non_decreasing = False
                    break

            if is_non_decreasing:
                return operations

            # 2️⃣ Find adjacent pair with minimum sum
            min_sum = float('inf')
            index = 0

            for i in range(len(nums) - 1):
                pair_sum = nums[i] + nums[i + 1]
                if pair_sum < min_sum:
                    min_sum = pair_sum
                    index = i

            # 3️⃣ Merge that pair
            nums = nums[:index] + [min_sum] + nums[index + 2:]

            # 4️⃣ Count operation
            operations += 1

        