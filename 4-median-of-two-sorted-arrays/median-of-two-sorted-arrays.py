class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        num3=sorted(nums1+nums2)
        if len(num3)%2!=0:
            a=len(num3)//2
            return num3[a]
        else:
            b=len(num3)//2
            c=num3[b]
            d=num3[b-1]
            e=(c+d)/2
            return e

        