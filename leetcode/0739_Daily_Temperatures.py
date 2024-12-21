class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        stack = []
        ans = [0] * len(temperatures)
        for i in range(len(temperatures) - 1, -1, -1):
            x = temperatures[i]
            while stack and temperatures[stack[-1]] <= x:
                stack.pop()
            if stack:
                ans[i] = stack[-1] - i
            stack.append(i)
        return ans

if __name__ == "__main__":
    s = Solution()
    print(s.dailyTemperatures([73,74,75,71,69,72,76,73]))
    print(s.dailyTemperatures([30,40,50,60]))
    print(s.dailyTemperatures([30,60,90]))

