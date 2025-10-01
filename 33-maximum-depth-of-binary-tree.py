class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    # WORKED ON MY MACHINE
    # def dfs(root, level=0,levelList=[]):
    #     levelList.append(level)
    #     if root is None:
    #         return 0
    #     if root.left or root.right:
    #         dfs(root.left, level + 1,levelList)
    #         dfs(root.right, level + 1,levelList)
    #     return (levelList)

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        return (1 + max(self.maxDepth(root.left),self.maxDepth(root.right)))
    