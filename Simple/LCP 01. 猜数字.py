'''
小A 和 小B 在玩猜数字。小B 每次从 1, 2, 3 中随机选择一个，小A 每次也从 1, 2, 3 中选择一个猜。他们一共进行三次这个游戏，请返回 小A 猜对了几次？
输入的guess数组为 小A 每次的猜测，answer数组为 小B 每次的选择。guess和answer的长度都等于3。

示例 1：
输入：guess = [1,2,3], answer = [1,2,3]
输出：3
解释：小A 每次都猜对了。
 
示例 2：
输入：guess = [2,2,3], answer = [3,2,1]
输出：1
解释：小A 只猜对了第二次。
 
限制：
guess的长度 = 3
answer的长度 = 3
guess的元素取值为 {1, 2, 3} 之一。
answer的元素取值为 {1, 2, 3} 之一。

'''

# 1.直接方法：
class Solution(object):
    def game(self, guess, answer):
        """
        :type guess: List[int]
        :type answer: List[int]
        :rtype: int
        """
        count = 0
        for i in range(len(answer)):
            if guess[i] == answer[i]:
                count = count + 1
            else:
                pass
        return count

# 2.布尔值相加的解法
class Solution:
    def game(self, guess: List[int], answer: List[int]) -> int:

        return (guess[0] == answer[0]) + (guess[1] == answer[1]) + (guess[2] == answer[2])

# 3.使用sum计算列表元素值相加和的解法
class Solution:
    def game(self, guess: List[int], answer: List[int]) -> int:

        return sum([guess[i] == answer[i] for i in range(0, len(answer))])

# 4.使用len获取列表长度的解法
class Solution:
    def game(self, guess: List[int], answer: List[int]) -> int:

        return len([guess[i] == answer[i] for i in range(0, len(answer))])

# 5.使用count计算列表元素值为True数量的解法
class Solution:
    def game(self, guess: List[int], answer: List[int]) -> int:

        return [guess[i] == answer[i] for i in range(0, len(answer))].count(True)
