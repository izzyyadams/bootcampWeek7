from collections import deque
class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        freshCount = 0
        twoIndexes = deque([])
        rowRange = len(grid)
        columnRange = len(grid[0])
        minutes = -1
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    freshCount += 1
                elif grid[i][j] == 2:
                    twoIndexes.append((i, j))
        if freshCount == 0:
            return 0
        
        while twoIndexes:
            indexCount = len(twoIndexes)
            for i in range(indexCount):
                currentTwo = twoIndexes.popleft()
                #left
                leftIndex = (currentTwo[0], currentTwo[1]-1)
                if (-1 < leftIndex[1] < columnRange) and grid[leftIndex[0]][leftIndex[1]] ==1:
                    grid[leftIndex[0]][leftIndex[1]] = 2
                    freshCount -= 1
                    twoIndexes.append(leftIndex)
                #right
                rightIndex= (currentTwo[0], currentTwo[1]+1)
                if (-1 < rightIndex[1] < columnRange) and grid[rightIndex[0]][rightIndex[1]] ==1:
                    grid[rightIndex[0]][rightIndex[1]] = 2
                    freshCount -= 1
                    twoIndexes.append(rightIndex)
                #up
                upIndex = (currentTwo[0]-1, currentTwo[1])
                if (-1 < upIndex[0] < rowRange) and grid[upIndex[0]][upIndex[1]] ==1:
                    grid[upIndex[0]][upIndex[1]] = 2
                    freshCount -= 1
                    twoIndexes.append(upIndex)
                #down
                downIndex= (currentTwo[0]+1, currentTwo[1])
                if (-1 < downIndex[0] < rowRange) and grid[downIndex[0]][downIndex[1]] ==1:
                    grid[downIndex[0]][downIndex[1]] = 2
                    freshCount -= 1
                    twoIndexes.append(downIndex)
            minutes += 1    
        
        if freshCount > 0:
            return -1
        else:
            return minutes 
