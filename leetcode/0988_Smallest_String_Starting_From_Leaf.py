from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        paths = []
        self.getAllPaths(paths, [], root)
        paths = [ "".join(list(map(lambda t: chr(t.val + 97), path)))[::-1] for path in paths ]
        return min(paths)

    def getAllPaths(self, res: list[list[TreeNode]], curr: list[TreeNode], root: TreeNode) -> None:
        if not (root.left or root.right):
            res.append(curr + [root])
        if root.left:
            self.getAllPaths(res, curr + [root], root.left)
        if root.right:
            self.getAllPaths(res, curr + [root], root.right)

if __name__ == "__main__":
    nodes = list(map(lambda x: TreeNode(x), [0, 1, 2, 3, 4, 3, 4]))
    nodes[0].left = nodes[1]
    nodes[0].right = nodes[2]
    nodes[1].left = nodes[3]
    nodes[1].right = nodes[4]
    nodes[2].left = nodes[5]
    nodes[2].right = nodes[6]
    root = nodes[0]
    s = Solution()
    print(s.smallestFromLeaf(root))
    print()
    root1 = TreeNode(19)
    root1.left = TreeNode(10)
    print(s.smallestFromLeaf(root1))