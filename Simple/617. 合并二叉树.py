'''
给定两个二叉树，想象当你将它们中的一个覆盖到另一个上时，两个二叉树的一些节点便会重叠。
你需要将他们合并为一个新的二叉树。合并的规则是如果两个节点重叠，那么将他们的值相加作为节点合并后的新值，否则不为 NULL 的节点将直接作为新二叉树的节点。

示例 1:
输入:
	Tree 1                     Tree 2
          1                         2
         / \                       / \
        3   2                     1   3
       /                           \   \
      5                             4   7
输出:
合并后的树:
	     3
	    / \
	   4   5
	  / \   \
	 5   4   7
注意: 合并必须从两个树的根节点开始。
'''

# 递归实现
class Solution(object):
	def mergeTrees(self, t1, t2):
		"""
		:type t1: TreeNode
		:type t2: TreeNode
		:rtype: TreeNode
		"""
		def dfs(r1,r2):
			# 如果 r1和r2中，只要有一个是null，函数就直接返回
			if not (r1 and r2):
				return r1 if r1 else r2
			# 让r1的值 等于  r1和r2的值累加
			# 再递归的计算两颗树的左节点、右节点
			r1.val += r2.val
			r1.left = dfs(r1.left,r2.left)
			r1.right = dfs(r1.right,r2.right)
			return r1
		return dfs(t1,t2)

# 迭代实现
class Solution(object):
	def mergeTrees(self, t1, t2):
		"""
		:type t1: TreeNode
		:type t2: TreeNode
		:rtype: TreeNode
		"""
	# 如果 t1和t2中，只要有一个是null，函数就直接返回
		if not (t1 and t2):
			return t2 if not t1 else t1
		queue = [(t1,t2)]
		while queue:
			r1,r2 = queue.pop(0)
			r1.val += r2.val
			# 如果r1和r2的左子树都不为空，就放到队列中
			# 如果r1的左子树为空，就把r2的左子树挂到r1的左子树上
			if r1.left and r2.left:
				queue.append((r1.left,r2.left))
			elif not r1.left:
				r1.left = r2.left
			# 对于右子树也是一样的
			if r1.right and r2.right:
				queue.append((r1.right,r2.right))
			elif not r1.right:
				r1.right = r2.right
		return t1