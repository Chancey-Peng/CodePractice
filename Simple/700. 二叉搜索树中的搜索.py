'''
给定二叉搜索树（BST）的根节点和一个值。 你需要在BST中找到节点值等于给定值的节点。 返回以该节点为根的子树。 如果节点不存在，则返回 NULL。

例如，
给定二叉搜索树:

        4
       / \
      2   7
     / \
    1   3

和值: 2
你应该返回如下子树:

      2
     / \
    1   3
在上述示例中，如果要找的值是 5，但因为没有节点值为 5，我们应该返回 NULL。
'''

"""
方法一：递归
算法

递归实现非常简单：
如果根节点为空 root == null 或者根节点的值等于搜索值 val == root.val，返回根节点。
如果 val < root.val，进入根节点的左子树查找 searchBST(root.left, val)。
如果 val > root.val，进入根节点的右子树查找 searchBST(root.right, val)。
返回根节点。
"""
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def searchBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        if root is None or val == root.val:
            return root
        return self.searchBST(root.left, val) if val < root.val else self.searchBST(root.right, val)
"""
方法二：迭代
为了降低空间复杂度，将递归转换为迭代：
如果根节点不空 root != null 且根节点不是目的节点 val != root.val：
如果 val < root.val，进入根节点的左子树查找 root = root.left。
如果 val > root.val，进入根节点的右子树查找 root = root.right。
返回 root
"""
