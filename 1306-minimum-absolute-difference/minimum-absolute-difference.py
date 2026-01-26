class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        b=float('inf')
        c=[]
        for i in range(1,len(arr)):
            d=arr[i]-arr[i-1]
            if d<b:
                b=d
                c=[[arr[i-1],arr[i]]]
            elif d==b:
                c.append([arr[i-1],arr[i]])
        return c
        