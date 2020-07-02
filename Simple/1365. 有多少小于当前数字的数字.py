'''
给你一个数组 nums，对于其中每个元素 nums[i]，请你统计数组中比它小的所有数字的数目。
换而言之，对于每个 nums[i] 你必须计算出有效的 j 的数量，其中 j 满足 j != i 且 nums[j] < nums[i] 。
以数组形式返回答案。

示例 1：
输入：nums = [8,1,2,2,3]
输出：[4,0,1,1,3]
解释：
对于 nums[0]=8 存在四个比它小的数字：（1，2，2 和 3）。
对于 nums[1]=1 不存在比它小的数字。
对于 nums[2]=2 存在一个比它小的数字：（1）。
对于 nums[3]=2 存在一个比它小的数字：（1）。
对于 nums[4]=3 存在三个比它小的数字：（1，2 和 2）。

示例 2：
输入：nums = [6,5,4,8]
输出：[2,1,0,3]

示例 3：
输入：nums = [7,7,7,7]
输出：[0,0,0,0]
 
提示：
2 <= nums.length <= 500
0 <= nums[i] <= 100
'''
# 枚举数组
class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        vec = [0] * n
        for i in range(n):
            vec[i] = sum(1 for j in range(n) if nums[j] < nums[i])
        return vec

# 频次数组+前缀和（最优）
class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        cnt, vec = [0] * 101, [0] * n
        for num in nums:
            cnt[num] += 1
        for i in range(1,101):
            cnt[i] += cnt[i-1]
        for i in range(n):
            if nums[i]:
                vec[i] = cnt[nums[i] - 1]
        return vec

# 排序
class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        vec = [0] * n
        tmp = sorted([(nums[i], i) for i in range(n)])

        pre = -1
        for i in range(n):
            if i != 0 and tmp[i][0] != tmp[i-1][0]:
                pre = i - 1
            vec[tmp[i][1]] = pre + 1
        return vec

class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        sortarr=sorted(nums)
        return [sortarr.index(i) for i in nums]

# 字典
class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        nums2 = sorted(nums)    # 对nums排序
        mapping = {}            # mapping储存num和其序号的键值对
        for i, num in enumerate(nums2):         # 遍历排序后的数组
            if i > 0 and nums2[i] == nums2[i-1]:# 如果某一位跟前一位的值相等，那么它的序号跟前一位一样（并列）
                mapping[nums2[i]] = mapping[nums2[i-1]]
            else:                               # 如果某一位跟前一位的值不等，那么以index为序号
                mapping[nums2[i]] = i
        res = []
        for num in nums:
            res.append(mapping[num])            # res用来储存返回值
        return res

nums = [8,1,2,2,3]
nums2 = sorted(nums)    # 对nums排序
mapping = {}            # mapping储存num和其序号的键值对
for i, num in enumerate(nums2):         # 遍历排序后的数组
    if i > 0 and nums2[i] == nums2[i-1]:# 如果某一位跟前一位的值相等，那么它的序号跟前一位一样（并列）
        mapping[nums2[i]] = mapping[nums2[i-1]]
        print(mapping[nums2[i]])
    else:                               # 如果某一位跟前一位的值不等，那么以index为序号
        mapping[nums2[i]] = i
        print(mapping[nums2[i]])
print(mapping)
res = []
for num in nums:
    res.append(mapping[num])            # res用来储存返回值
print(res)

