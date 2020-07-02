'''
给你一个有效的 IPv4 地址 address，返回这个 IP 地址的无效化版本。
所谓无效化 IP 地址，其实就是用 "[.]" 代替了每个 "."。

示例 1：
输入：address = "1.1.1.1"
输出："1[.]1[.]1[.]1"

示例 2：
输入：address = "255.100.50.0"
输出："255[.]100[.]50[.]0"
 
提示：
给出的 address 是一个有效的 IPv4 地址
'''

# 正则表达式解题
import re
class Solution(object):
    def defangIPaddr(self, address):
        """
        :type address: str
        :rtype: str
        """
        return re.sub('\.', '[.]', address)

# 使用replace解题
class Solution(object):
    def defangIPaddr(self, address):
        """
        :type address: str
        :rtype: str
        """
        return address.replace(".", "[.]")

# 使用字符串判断
class Solution(object):
    def defangIPaddr(self, address):
        """
        :type address: str
        :rtype: str
        """
        b = ""
        for i in (address):
            if i != '.':
                b = b + i
            else:
                b = b + '[.]'
        return b