class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()  
        c = []
        for i in range(len(nums)-2):
            if i>0 and nums[i]==nums[i-1]:
                continue
            l=i+1
            r=len(nums)-1
            while (l<r):
                sum1=nums[i]+nums[l]+nums[r]
                if sum1==0:
                    c.append([nums[i],nums[l],nums[r]])
                    left_val, right_val = nums[l], nums[r]
                    l+=1
                    r-=1
                    while l < r and nums[l] == left_val:
                        l += 1
                    while l < r and nums[r] == right_val:
                        r -= 1
                elif sum1<0:
                    l+=1
                else:
                    r-=1
        return c



   





        
        
        