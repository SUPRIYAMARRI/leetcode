class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        a=0
        for i in range(len(arr1)):
            b=True
            for j in range(len(arr2)):
                if abs(arr1[i]-arr2[j])<=d:
                    b=False
            if b:
                a+=1
        return a
                    
                