from functools import reduce
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root is None:
            return False
        paths = []
        self.getAllPaths(paths, [], root)
        paths = [ [ node.val for node in path] for path in paths]
        for path in paths:
            if sum(path) == targetSum:
                return True
        return False

    def getAllPaths(self, res: list[list[TreeNode]], curr: list[TreeNode], root: TreeNode) -> None:
            if not (root.left or root.right):
                res.append(curr + [root])
            if root.left:
                self.getAllPaths(res, curr + [root], root.left)
            if root.right:
                self.getAllPaths(res, curr + [root], root.right)