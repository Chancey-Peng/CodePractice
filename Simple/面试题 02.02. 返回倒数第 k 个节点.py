'''
实现一种算法，找出单向链表中倒数第 k 个节点。返回该节点的值。
注意：本题相对原题稍作改动

示例：
输入： 1->2->3->4->5 和 k = 2
输出： 4
说明：
给定的 k 保证是有效的。
'''
# 快慢指针
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def kthToLast(self, head: ListNode, k: int) -> int:
        target_node = head                      # 慢指针
        fast_node = head                        # 快指针
        steps = 0                               # 记录快指针的步数
        while fast_node:                        # 到尾结点时退出循环
            fast_node = fast_node.next          # 快指针移动一步
            if steps>=k:                        # 慢指针开始移动条件判断
                target_node = target_node.next  # 慢指针移动一步
            steps += 1                          # 累加步数
        return target_node.val                  # 返回目标节点的值

# 哨兵节点+快慢指针
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def kthToLast(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: int
        """
        if not head:
            return

        # 对于涉及到寻找节点的下一个的下一个节点的链表题目，我们都可以构造一个虚拟节点指向表头，
        # 方便代码边界的处理，比如列表为[1]的情况，就不用担心空异常
        dummy = ListNode(-1)
        dummy.next = head

        # 双指针
        pre = dummy
        cur = dummy

        # 一个指针先走k步
        for i in range(k):
            cur = cur.next

        # 然后两个指针同时向前走，直到其中一个指针走到表尾，
        # 此时另外一个指针的下一个就是要寻找的目标节点
        while cur.next:
            pre = pre.next
            cur = cur.next

        return pre.next.val