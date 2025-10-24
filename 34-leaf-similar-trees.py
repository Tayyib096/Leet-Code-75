# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        
        leaf1=[]
        leaf2=[]
        
        def get_leaf(root, result):
            if root.left is None and root.right is None:
                result.append(root.val)
                return
            if root.left:
                get_leaf(root.left, result)
            if root.right:
                get_leaf(root.right, result) 
            return


        get_leaf(root1,leaf1)
        get_leaf(root2,leaf2)

        return (leaf1 == leaf2)