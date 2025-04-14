class Solution:
    def countGoodTriplets(self, arr: list[int], a: int, b: int, c: int) -> int:
        count = 0
        for i in range(len(arr)):
            p = arr[i]
            for j in range(i + 1, len(arr)):
                q = arr[j]
                for k in range(j + 1, len(arr)):
                    r = arr[k]
                    if abs(q - p) > a:
                        continue
                    if abs(r - q) > b:
                        continue
                    if abs(r - p) > c:
                        continue
                    count += 1
        return count
    
if __name__ == "__main__":
    s = Solution()
    print(s.countGoodTriplets([3, 0, 1, 1, 9, 7], 7, 2, 3))
    print(s.countGoodTriplets([1, 1, 2, 2, 3], 0, 0, 1))

                    