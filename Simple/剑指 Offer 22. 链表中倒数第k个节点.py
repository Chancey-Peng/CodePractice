'''
输入一个链表，输出该链表中倒数第k个节点。为了符合大多数人的习惯，本题从1开始计数，即链表的尾节点是倒数第1个节点。例如，一个链表有6个节点，从头节点开始，它们的值依次是1、2、3、4、5、6。这个链表的倒数第3个节点是值为4的节点。

示例：
给定一个链表: 1->2->3->4->5, 和 k = 2.
返回链表 4->5.
'''

# 方法一：
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getKthFromEnd(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head:
            return

        # 初始化快慢指针
        pre = head
        cur = head

        # 快指针先走k步
        for _ in range(k):
            cur = cur.next
            # 如果走到头了，直接返回表头
            if not cur:
                return pre

        # 快慢指针同时向前走
        while cur:
            pre = pre.next
            cur = cur.next

        return pre

# 方法二：
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getKthFromEnd(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        result = head
        temp = head
        num = 1
        while num != k and temp:
            temp = temp.next
            num += 1
        if num != k:# 判断是否存在倒数第K个节点
            return None
        while temp.next:
            result = result.next
            temp = temp.next
        return result