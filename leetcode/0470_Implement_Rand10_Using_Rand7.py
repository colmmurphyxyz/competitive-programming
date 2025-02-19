from random import randint

def rand7() -> int:
    return randint(1, 7)

class Solution:
    def rand10(self) -> int:
        ret = float("inf")
        while ret >= 40:
            ret = (rand7() - 1) * 7 + rand7() - 1
        return (ret % 10) + 1
    
if __name__ == "__main__":
    s = Solution()
    for _ in range(20):
        print(s.rand10())