class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        c=[]
        for i in range(len(nums2)):
            if nums2[i] in nums1:
                if nums2[i] not in c:
                    c.append(nums2[i])
        return c