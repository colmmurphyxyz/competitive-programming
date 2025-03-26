from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.isvalid(root, float("-inf"), float("inf"))
    
    def isValid(self, root: Optional[TreeNode], left, right) -> bool:
        if root is None:
            return True
        if root.val <= left or root.val >= right:
            return False
        if root.left is not None and root.left.val >= root.val:
            return False
        if root.right is not None and root.right.val <= root.val:
            return False
        return self.isValid(root.left, left, min(right, root.val)) \
            and self.isValid(root.right, max(left, root.val), right)
    
