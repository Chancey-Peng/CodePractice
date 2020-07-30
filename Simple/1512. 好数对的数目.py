'''
给你一个整数数组 nums 。
如果一组数字 (i,j) 满足 nums[i] == nums[j] 且 i < j ，就可以认为这是一组 好数对 。
返回好数对的数目。


示例 1：
输入：nums = [1,2,3,1,1,3]
输出：4
解释：有 4 组好数对，分别是 (0,3), (0,4), (3,4), (2,5) ，下标从 0 开始

示例 2：
输入：nums = [1,1,1,1]
输出：6
解释：数组中的每组数字都是好数对

示例 3：
输入：nums = [1,2,3]
输出：0
 
提示：
1 <= nums.length <= 100
1 <= nums[i] <= 100
'''
import collections

"""
方法一：暴力统计
思路与算法

对于每个 a_i，枚举所有的 a_j (j > i)，检查是否满足 a_i = a_j	,如果是就计入答案。
"""

class Solution(object):
    def numIdenticalPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = 0
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] == nums[j]:
                    ans += 1
        return ans

"""
方法二：组合计数
思路与算法

用哈希表统计每个数在序列中出现的次数，假设数字 k 在序列中出现的次数为 v，
那么满足题目中所说的 nums[i]=nums[j]=k(i<j) 的 (i, j) 的数量就是 v(v−1)/2，即 k 这个数值对答案的贡献是 v(v−1)/2。
我们只需要把所有数值的贡献相加，即可得到答案。
"""

class Solution(object):
    def numIdenticalPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        m = collections.Counter(nums)
        return sum(v *(v-1)//2 for k,v in m.items())