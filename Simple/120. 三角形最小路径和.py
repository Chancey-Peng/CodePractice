'''
给定一个三角形，找出自顶向下的最小路径和。每一步只能移动到下一行中相邻的结点上。
相邻的结点 在这里指的是 下标 与 上一层结点下标 相同或者等于 上一层结点下标 + 1 的两个结点。

例如，给定三角形：
[
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]
自顶向下的最小路径和为 11（即，2 + 3 + 5 + 1 = 11）。

说明：
如果你可以只使用 O(n) 的额外空间（n 为三角形的总行数）来解决这个问题，那么你的算法会很加分。
'''

"""
方法：动态规划 + 空间优化
思路与算法
在题目描述中的「说明」部分，提到了可以将空间复杂度优化至 O(n)。
我们回顾方法一中的状态转移方程：

                f[i−1][0]+c[i][0],  j=0
f[i][j]=        f[i−1][i−1]+c[i][i],    j=i
                min(f[i−1][j−1],f[i−1][j])+c[i][j], otherwise
​	
可以发现，f[i][j] 只与 f[i-1][..] 有关，而与 f[i-2][..] 及之前的状态无关，因此我们不必存储这些无关的状态。具体地，我们使用两个长度为 n 的一维数组进行转移，将 i 根据奇偶性映射到其中一个一维数组，那么 i-1 就映射到了另一个一维数组。这样我们使用这两个一维数组，交替地进行状态转移。
"""


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        f = [[0] * n for _ in range(2)]
        f[0][0] = triangle[0][0]

        for i in range(1, n):
            curr, prev = i % 2, 1 - i % 2
            f[curr][0] = f[prev][0] + triangle[i][0]
            for j in range(1, i):
                f[curr][j] = min(f[prev][j - 1], f[prev][j]) + triangle[i][j]
            f[curr][i] = f[prev][i - 1] + triangle[i][i]

        return min(f[(n - 1) % 2])

"""
为什么只有在递减地枚举 j 时，才能省去一个一维数组？当我们在计算位置 (i, j) 时，f[j+1] 到 f[i] 已经是第 i 行的值，而 f[0] 到 f[j] 仍然是第 i-1 行的值。此时我们直接通过
f[j]=min(f[j−1],f[j])+c[i][j]
进行转移，恰好就是在 (i-1, j-1) 和 (i-1, j) 中进行选择。但如果我们递增地枚举 j，那么在计算位置 (i, j) 时，f[0] 到 f[j-1] 已经是第 i 行的值。如果我们仍然使用上述状态转移方程，那么是在 (i, j-1) 和 (i-1, j) 中进行选择，就产生了错误。
"""


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        f = [0] * n
        f[0] = triangle[0][0]

        for i in range(1, n):
            f[i] = f[i - 1] + triangle[i][i]
            for j in range(i - 1, 0, -1):
                f[j] = min(f[j - 1], f[j]) + triangle[i][j]
            f[0] += triangle[i][0]

        return min(f)