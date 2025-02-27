from heapq import heappop, heappush

class Solution:
    # def lenLongestFibSubseq(self, arr: list[int]) -> int:
    #     subseqs: list[tuple[int, list[int]]] = []
    #     for i in range(len(arr)):
    #         for j in range(i + 1, len(arr)):
    #             subseq = [arr[i], arr[j]]
    #             for k in range(j + 1, len(arr)):
    #                 x = arr[k]
    #                 if x == subseq[-1] + subseq[-2]:
    #                     subseq.append(x)
    #             heappush(subseqs, (-len(subseq), subseq))
    #     return heappop(subseqs)

    def lenLongestFibSubseq(self, arr: list[int]) -> int:
        maxLen = 0
        dp = [ [ 0 for _ in range(len(arr)) ] for _ in range(len(arr)) ]
        valToIdx = {}

        for i, curr in enumerate(arr):
            valToIdx[curr] = i
            for j, prev in enumerate(arr[:i]):
                diff = curr - prev
                prevIdx = valToIdx.get(diff)
                if prevIdx is not None and diff < prev:
                    dp[j][i] = dp[prevIdx][j] + 1
                else:
                    dp[j][i] = 2
                maxLen = max(maxLen, dp[j][i])

        if maxLen < 3:
            return 0
        return maxLen
                
    
if __name__ == "__main__":
    s = Solution()
    print(s.lenLongestFibSubseq([1, 2, 3, 4, 5, 6, 7, 8]))
    print(s.lenLongestFibSubseq([1, 3, 7, 11, 12, 14, 18]))