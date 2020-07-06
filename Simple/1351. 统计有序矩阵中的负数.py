'''
给你一个 m * n 的矩阵 grid，矩阵中的元素无论是按行还是按列，都以非递增顺序排列。 
请你统计并返回 grid 中 负数 的数目。

示例 1：
输入：grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]
输出：8
解释：矩阵中共有 8 个负数。

示例 2：
输入：grid = [[3,2],[1,0]]
输出：0

示例 3：
输入：grid = [[1,-1],[-1,-1]]
输出：3

示例 4：
输入：grid = [[-1]]
输出：1
 

提示：
m == grid.length
n == grid[i].length
1 <= m, n <= 100
-100 <= grid[i][j] <= 100
'''
class Solution(object):
    def f(self,A):
        count = 0
        for i in A:
            count += 1 if i < 0 else 0
    def countNegatives(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        grid = list(map(lambda x:self.f(x),grid))
        return sum(grid)

import numpy as np
class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        return int((np.array(grid)<0).sum())