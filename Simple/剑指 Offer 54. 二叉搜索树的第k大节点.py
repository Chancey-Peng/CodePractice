'''
给定一棵二叉搜索树，请找出其中第k大的节点。

示例 1:
输入: root = [3,1,4,null,2], k = 1
   3
  / \
 1   4
  \
   2
输出: 4

示例 2:
输入: root = [5,3,6,2,4,null,null,1], k = 3
       5
      / \
     3   6
    / \
   2   4
  /
 1
输出: 4
 

限制：
1 ≤ k ≤ 二叉搜索树元素个数
'''

"""
递归解析：
终止条件： 当节点 rootroot 为空（越过叶节点），则直接返回；
递归右子树： 即 dfs(root.right)dfs(root.right) ；
三项工作：
提前返回： 若 k = 0k=0 ，代表已找到目标节点，无需继续遍历，因此直接返回；
统计序号： 执行 k = k - 1k=k−1 （即从 kk 减至 00 ）；
记录结果： 若 k = 0k=0 ，代表当前节点为第 kk 大的节点，因此记录 res = root.valres=root.val ；
递归左子树： 即 dfs(root.left)dfs(root.left) 
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def kthLargest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        def dfs(root):
            if not root: return
            dfs(root.right)
            if self.k == 0: return
            self.k -= 1
            if self.k == 0: self.res = root.val
            dfs(root.left)
        self.k = k
        dfs(root)
        return self.res