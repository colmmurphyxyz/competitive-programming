from typing import Optional
from copy import deepcopy


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self) -> str:
        return f"<{self.val}>"
    
    __repr__ = __str__

class Solution:
    def allPossibleFBT(self, n: int) -> list[Optional[TreeNode]]:
        if n % 2 == 0:
            # no FBT can have an even number of nodes, except for the empty tree
            return []
        
        dp = [ [] for _ in range(n + 1) ]
        dp[1].append(TreeNode(0))

        for count in range(3, n + 1, 2):
            for i in range(1, count - 1, 2):
                j = count - 1 - i
                for left in dp[i]:
                    for right in dp[j]:
                        root = TreeNode(0, left, right)
                        dp[count].append(root)
        return dp[n]
    
if __name__ == "__main__":
    s = Solution()
    print(s.allPossibleFBT(1))
    print(s.allPossibleFBT(2))
    print(s.allPossibleFBT(3))
    print(s.allPossibleFBT(7))