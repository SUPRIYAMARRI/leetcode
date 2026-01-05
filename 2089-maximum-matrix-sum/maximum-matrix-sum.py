class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        s=0
        total=0 
        m=float('inf')
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                val=matrix[i][j]
                if val<0:
                    s+=1
                total+=abs(val)
                m=min(m,abs(val))          
        if s%2==0:
            return total
        else:
            return total-2*m


