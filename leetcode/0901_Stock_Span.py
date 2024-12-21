class StockSpanner:
    def __init__(self):
        self._stack: list[int] = []

    def next(self, price: int) -> int:
        count: int = 1
        while self._stack and self._stack[-1][0] <= price:
            (_, span) = self._stack.pop()
            count += span
        self._stack.append((price, count))
        return count
    
if __name__ == "__main__":
    s1 = StockSpanner()
    for p in [100, 80, 60, 70, 60, 75, 85]:
        print(s1.next(p), end=" ")
    print()
    s2 = StockSpanner()
    for p in [28, 14, 28, 35, 56, 53, 66, 80, 87, 88]:
        print(s2.next(p), end=" ")