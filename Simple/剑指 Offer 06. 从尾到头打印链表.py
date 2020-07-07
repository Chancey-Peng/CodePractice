'''
输入一个链表的头节点，从尾到头反过来返回每个节点的值（用数组返回）。

示例 1：
输入：head = [1,3,2]
输出：[2,3,1]
 
限制：
0 <= 链表长度 <= 10000
'''

# 反转解题
class Solution:
    def reversePrint(self, head: ListNode) -> List[int]:
        res = []
        while head:
            res.append(head.val)
            head = head.next
        return res[::-1]  # 或者 reverse(res)

# 递归解法
class Solution:
    def reversePrint(self, head: ListNode) -> List[int]:
        if not head: return []
        return self.reversePrint(head.next) + [head.val]

# 堆栈解题
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reversePrint(self, head):
        """
        :type head: ListNode
        :rtype: List[int]
        """
        stack = []
        while head: # push
            stack.append(head.val)
            head = head.next
        res = []
        while stack: # pop
            res.append(stack.pop())
        return res