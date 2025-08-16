class Solution(object):
    def equalPairs(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n = len(grid)
        pairs = 0
        rows = dict()

        for row in grid:
            if tuple(row) not in rows :
                rows[tuple(row)]=1
            else:
                rows[tuple(row)] +=1
        for col in range(n):
            column = tuple(grid[r][col] for r in range(n))
            print(column)
            if column in rows:
                pairs += rows[column]
        return(pairs)