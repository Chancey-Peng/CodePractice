'''
给你一个数组 prices ，其中 prices[i] 是商店里第 i 件商品的价格。
商店里正在进行促销活动，如果你要买第 i 件商品，那么你可以得到与 prices[j] 相等的折扣，其中 j 是满足 j > i 且 prices[j] <= prices[i] 的 最小下标 ，如果没有满足条件的 j ，你将没有任何折扣。
请你返回一个数组，数组中第 i 个元素是折扣后你购买商品 i 最终需要支付的价格。

示例 1：
输入：prices = [8,4,6,2,3]
输出：[4,2,4,2,3]
解释：
商品 0 的价格为 price[0]=8 ，你将得到 prices[1]=4 的折扣，所以最终价格为 8 - 4 = 4 。
商品 1 的价格为 price[1]=4 ，你将得到 prices[3]=2 的折扣，所以最终价格为 4 - 2 = 2 。
商品 2 的价格为 price[2]=6 ，你将得到 prices[3]=2 的折扣，所以最终价格为 6 - 2 = 4 。
商品 3 和 4 都没有折扣。

示例 2：
输入：prices = [1,2,3,4,5]
输出：[1,2,3,4,5]
解释：在这个例子中，所有商品都没有折扣。

示例 3：
输入：prices = [10,1,1,6]
输出：[9,0,1,6]

提示：
1 <= prices.length <= 500
1 <= prices[i] <= 10^3
'''

class Solution:
    def finalPrices(self, prices):
        _prices = []
        l = len(prices)
        #i 为当前元素
        for i in range(l):
            #n是i后面的元素
            n = i + 1
            #遍历从n开始
            for j in range(n,l):
                #遇到小于等于i的元素就相减，结果添加到数组，添加后退出当前循环，开始下个元素
                if prices[i] >= prices[j]:
                    _prices.append(prices[i] - prices[j])
                    break
            # 此次遍历没有找到比i小的，说明没有折扣，添加i
            else:
                _prices.append(prices[i])
        return _prices