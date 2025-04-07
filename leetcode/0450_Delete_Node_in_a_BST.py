from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        candidate = self.searchBST(root, key)
        if candidate is None:
            return root
        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        else:
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left
            
            min_node = self.findMin(root.right)
            root.val = min_node.val
            root.right = self.deleteNode(root.right, root.val)

        return root
    
    def findMin(self, root: TreeNode) -> TreeNode:
        while root.left is not None:
            root = root.left
        return root

