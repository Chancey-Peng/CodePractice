'''
请完成一个函数，输入一个二叉树，该函数输出它的镜像。

例如输入：

     4
   /   \
  2     7
 / \   / \
1   3 6   9
镜像输出：

     4
   /   \
  7     2
 / \   / \
9   6 3   1

示例 1：
输入：root = [4,2,7,1,3,6,9]
输出：[4,7,2,9,6,3,1]
 
限制：
0 <= 节点个数 <= 1000
'''

'''方法一：递归法
根据二叉树镜像的定义，考虑递归遍历（dfs）二叉树，交换每个节点的左 / 右子节点，即可生成二叉树的镜像。
递归解析：
终止条件： 当节点 rootroot 为空时（即越过叶节点），则返回 nullnull ；
递推工作：
初始化节点 tmptmp ，用于暂存 rootroot 的左子节点；
开启递归 右子节点 mirrorTree(root.right)mirrorTree(root.right) ，并将返回值作为 rootroot 的 左子节点 。
开启递归 左子节点 mirrorTree(tmp)mirrorTree(tmp) ，并将返回值作为 rootroot 的 右子节点 。
返回值： 返回当前节点 rootroot ；
'''
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution(object):
    def mirrorTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root: return
        tmp = root.left
        root.left = self.mirrorTree(root.right)
        root.right = self.mirrorTree(tmp)
        return root

'''
方法二：辅助栈（或队列）
利用栈（或队列）遍历树的所有节点 nodenode ，并交换每个 nodenode 的左 / 右子节点。
算法流程：
特例处理： 当 rootroot 为空时，直接返回 nullnull ；
初始化： 栈（或队列），本文用栈，并加入根节点 rootroot 。
循环交换： 当栈 stackstack 为空时跳出；
出栈： 记为 nodenode ；
添加子节点： 将 nodenode 左和右子节点入栈；
交换： 交换 nodenode 的左 / 右子节点。
返回值： 返回根节点 rootroot 。
'''
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def mirrorTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root: return
        stack = [root]
        while stack:
            node = stack.pop()
            if node.left:stack.append(node.left)
            if node.right:stack.append(node.right)
            node.left,node.right=node.right,node.left
        return root