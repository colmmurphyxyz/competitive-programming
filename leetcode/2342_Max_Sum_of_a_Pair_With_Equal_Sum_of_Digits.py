import heapq

class Solution:
    def _digitSum(num: int) -> int:
        subtotal = 0
        while num > 0:
            p, q = divmod(num, 10)
            num = p
            subtotal += q
        return subtotal
    
    def maximumSum(self, nums: list[int]) -> int:
        digitSums: dict[int, list[int]] = {}
        for num in nums:
            s = Solution._digitSum(num)
            matchingSums = digitSums.get(s, [])
            heapq.heappush(matchingSums, -num)
            digitSums[s] = matchingSums
        maxSum = -1
        for v in digitSums.values():
            if len(v) < 2:
                continue
            a = heapq.heappop(v)
            b = heapq.heappop(v)
            maxSum = max(maxSum, -(a + b))
        return maxSum

if __name__ == "__main__":
    s = Solution()
    print(s.maximumSum([18, 43, 36, 13, 7]))
    print(s.maximumSum([10, 12, 19, 14]))