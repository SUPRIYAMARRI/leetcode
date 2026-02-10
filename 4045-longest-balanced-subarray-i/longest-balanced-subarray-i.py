class Solution:
    def longestBalanced(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0

        for i in range(n):
            s = []   # stores distinct even numbers
            g = []   # stores distinct odd numbers
            c = 0    # count of distinct even numbers
            d = 0    # count of distinct odd numbers

            for j in range(i, n):
                x = nums[j]

                if x % 2 == 0:
                    if x not in s:
                        s.append(x)
                        c += 1
                else:
                    if x not in g:
                        g.append(x)
                        d += 1

                if c == d:
                    ans = max(ans, j - i + 1)

        return ans
