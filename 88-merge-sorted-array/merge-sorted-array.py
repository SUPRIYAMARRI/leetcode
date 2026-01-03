class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        k=m
        if n>0:
            for i in range(len(nums2)):
                nums1[k]=nums2[i]
                k+=1
            return nums1.sort()
        else:
            return nums1
        
            
            

        