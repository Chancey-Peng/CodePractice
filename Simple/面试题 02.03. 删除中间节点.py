'''
实现一种算法，删除单向链表中间的某个节点（即不是第一个或最后一个节点），假定你只能访问该节点。

示例：
输入：单向链表a->b->c->d->e->f中的节点c
结果：不返回任何数据，但该链表变为a->b->d->e->f
'''


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        if not node or not node.next:
            return

        # 保存将要被删除的节点，防止删除之后找不到
        dummy = node.next
        # 删除当前节点的下一个节点
        node.next = node.next.next
        # 将已经被删除掉的下一个节点的值赋值给真实需要被删除的节点
        node.val = dummy.val