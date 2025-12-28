class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l=0
        r=len(nums)-1
        d=[-1,-1]
        while l<=r and nums[l]!=target:
            l+=1
        while l<=r and nums[r]!=target:
            r-=1
        if l<=r:
            return [l,r]  
        return d
                
        