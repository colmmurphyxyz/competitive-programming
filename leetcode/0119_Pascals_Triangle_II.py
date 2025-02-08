from math import ceil

class Solution:
    def getRow(self, rowIndex: int) -> list[int]:
        if rowIndex == 0:
            return [1]
        if rowIndex == 1:
            return [1, 1]
        current_row = [1, 1]
        def dp():
            new_row = [1]
            # as each row in Pascals Triangle is symmetric
            # we only need to compute one half
            for i in range(len(current_row) // 2):
                new_row.append(current_row[i] + current_row[i + 1])
            # 'flip' the list to obtain the other half
            if len(current_row) % 2 != 0:
                new_row += reversed(new_row)
            else:
                new_row += reversed(new_row[:-1])
            return new_row
        
        for _ in range(1, rowIndex):
            current_row = dp()
        return current_row
    
if __name__ == "__main__":
    s = Solution()
    print(s.getRow(0))
    print(s.getRow(1))
    print(s.getRow(2))
    print(s.getRow(3))
    print(s.getRow(4))