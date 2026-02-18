class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
      a=sum(range(1,len(nums)+1))
      b=sum(nums)
      c=sum(set(nums))
      return[b-c,a-c]

        