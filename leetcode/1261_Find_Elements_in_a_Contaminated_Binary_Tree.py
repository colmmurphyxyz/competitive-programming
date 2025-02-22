from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class FindElements:
    def __init__(self, root: Optional[TreeNode]):
        self.root: TreeNode = root
        self._tree_elements: set[int] = set()
        if self.root is not None:
            self._recover_tree(root, possible_value=0)

    def _recover_tree(self, root: TreeNode, possible_value: int):
        self._tree_elements.add(possible_value)
        if root.left is not None:
            self._recover_tree(root.left, 2 * possible_value + 1)
        if root.right:
            self._recover_tree(root.right, 2 * possible_value + 2)

    def find(self, target: int) -> bool:
        return target in self._tree_elements
    
if __name__ == "__main__":
    root = TreeNode(-1)
    left = TreeNode(-1)
    root.left = left
    left.left = TreeNode(-1)
    left.right = TreeNode(-1)
    root.right = TreeNode(-1)

    fe = FindElements(root)
    print(fe.find(1))
    print(fe.find(3))
    print(fe.find(5))
