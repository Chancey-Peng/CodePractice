'''
给定一个 N 叉树，返回其节点值的后序遍历。

例如，给定一个 3叉树 :
        1
       / \  \
      3   2  4
     / \
    5   6
返回其后序遍历: [5,6,3,2,4,1].

说明: 递归法很简单，你可以使用迭代法完成此题吗?
'''


"""
迭代方法：
在后序遍历中，我们会先遍历一个节点的所有子节点，再遍历这个节点本身。例如当前的节点为 u，它的子节点为 v1, v2, v3 时，那么后序遍历的结果为 [children of v1], v1, [children of v2], v2, [children of v3], v3, u，其中 [children of vk] 表示以 vk 为根节点的子树的后序遍历结果（不包括 vk 本身）。我们将这个结果反转，可以得到 u, v3, [children of v3]', v2, [children of v2]', v1, [children of v1]'，其中 [a]' 表示 [a] 的反转。此时我们发现，结果和前序遍历非常类似，只不过前序遍历中对子节点的遍历顺序是 v1, v2, v3，而这里是 v3, v2, v1。
因此我们可以使用和 N叉树的前序遍历 相同的方法，使用一个栈来得到后序遍历。我们首先把根节点入栈。当每次我们从栈顶取出一个节点 u 时，就把 u 的所有子节点顺序推入栈中。例如 u 的子节点从左到右为 v1, v2, v3，那么推入栈的顺序应当为 v1, v2, v3，这样就保证了下一个遍历到的节点（即 u 的第一个子节点 v3）出现在栈顶的位置。在遍历结束之后，我们把遍历结果反转，就可以得到后序遍历。
"""

# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
class Solution(object):
    def postorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        if root is None:
            return []
        stack, output = [root, ], []
        while stack:
            root = stack.pop()
            if root is not None:
                output.append(root.val)
            for c in root.children:
                stack.append(c)
        return output[::-1]

# 递归方法：
class Solution(object):
    def postorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        res = []
        if root == None: return res
        def recursion(root, res):
            for child in root.children:
                recursion(child, res)
            res.append(root.val)
        recursion(root, res)
        return res
