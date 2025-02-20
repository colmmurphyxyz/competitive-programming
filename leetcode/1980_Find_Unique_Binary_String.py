class Solution:
    def findDifferentBinaryString(self, nums: list[str]) -> str:
        n = len(nums)
        nums: set[int] = set([ int(k, 2) for k in nums] )
        ans: int = self.firstValidNum(nums, n, curr=0, length=0)
        return bin(ans)[2:].zfill(n)
    
    def firstValidNum(self, nums: set[int], n: int, curr: int, length: int) -> int:
        if length == n:
            if curr not in nums:
                return curr
        if length > n:
            return None
        ret = self.firstValidNum(nums, n, (curr << 1), length + 1)
        if ret is not None:
            return ret
        ret = self.firstValidNum(nums, n, (curr << 1) + 1, length + 1)
        return ret
    
if __name__ == "__main__":
    s = Solution()
    print(s.findDifferentBinaryString(["01", "10"]))
    print(s.findDifferentBinaryString(["111", "011", "001"]))
