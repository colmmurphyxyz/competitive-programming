class TreeNode:
    def __init__(self, val=0, xorTotal=0, left=None, right=None):
        self.val = val
        self.xorTotal = xorTotal
        self.left = left
        self.right = right

def dump(root: TreeNode, indent: str = ""):
    if root is None:
        return
    print(f"{indent}({root.val}, {root.xorTotal})")
    dump(root.left, indent + "    ")
    dump(root.right, indent + "    ")

class Solution:
    def subsetXORSum(self, nums: list[int]) -> int:
        root = TreeNode([], 0, None, None)
        res = self.buildSubsetTree(root, nums)
        return res

    def buildSubsetTree(self, root: TreeNode, nums: list[int]) -> None:
        if len(nums) == 0:
            return root.xorTotal
        root.left = TreeNode(root.val, root.xorTotal)
        root.right = TreeNode(root.val + [nums[0]], root.xorTotal ^ nums[0])
        return self.buildSubsetTree(root.left, nums[1:]) + \
            self.buildSubsetTree(root.right, nums[1:])

if __name__ == "__main__":
    s = Solution()
    print(s.subsetXORSum([1, 3]))
    print(s.subsetXORSum([5, 1, 6]))
    print(s.subsetXORSum([3, 4, 5, 6, 7, 8]))

