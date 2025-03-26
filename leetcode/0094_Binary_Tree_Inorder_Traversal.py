from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> list[int]:
        if root is None:
            return []
        return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right)
    
if __name__ == "__main__":
    s = Solution()
    root = TreeNode(1, None, TreeNode(2, TreeNode(3), None))
    print(s.inorderTraversal(root))
