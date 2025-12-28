class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        count=0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] >=0:
                    continue
                else:
                    count+=1
        return count

        