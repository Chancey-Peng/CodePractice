'''
输入两个递增排序的链表，合并这两个链表并使新链表中的节点仍然是递增排序的。

示例1：
输入：1->2->4, 1->3->4
输出：1->1->2->3->4->4
限制：

0 <= 链表长度 <= 1000
'''

"""解题思路：
根据题目描述， 链表l1, l2是 递增 的，因此容易想到使用双指针 l1和 l2遍历两链表，根据 l1.val和 l2.val 的大小关系确定节点添加顺序，两节点指针交替前进，直至遍历完毕。

引入伪头节点： 由于初始状态合并链表中无节点，因此循环第一轮时无法将节点添加到合并链表中。解决方案：初始化一个辅助节点 dumdum 作为合并链表的伪头节点，将各节点添加至 dumdum 之后。

算法流程：
初始化： 伪头节点 dum ，节点 cur 指向 dum 。
循环合并： 当l1或l2为空时跳出；
当l1.val<l2.val 时：cur 的后继节点指定为 l1，并 l1向前走一步；
当l1.val≥l2.val 时：cur 的后继节点指定为 l2，并 l2向前走一步 ；
节点 cur 向前走一步，即 cur = cur.next。

合并剩余尾部： 跳出时有两种情况，即 l1为空 或 l2为空。
若 l1!=null ： 将l1添加至节点 cur 之后；
否则： 将 l2添加至节点 cur 之后。
返回值： 合并链表在伪头节点 dum 之后，因此返回 dum.next 即可。
"""

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        cur = dum = ListNode(0)
        while l1 and l2:
            if l1.val < l2.val:
                cur.next, l1 = l1, l1.next
            else:
                cur.next, l2 = l2, l2.next
            cur = cur.next
        cur.next = l1 if l1 else l2
        return dum.next