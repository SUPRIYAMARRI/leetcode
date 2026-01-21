from typing import List

class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        result = []
        for n in nums:
            if n % 2 == 0:
                result.append(-1)
            else:
                x = n
                bit = 1
                # find the rightmost 0 in n's trailing bits
                while x & bit:
                    bit <<= 1
                # subtract the last 1 bit from n
                x = n - (bit >> 1)
                result.append(x)
        return result
