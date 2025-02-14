class ProductOfNumbers:
    def __init__(self):
        self._products = []

    def add(self, num: int) -> None:
        if num == 0:
            self._products = []
        elif self._products:
            self._products.append(self._products[-1] * num)
        else:
            self._products.append(num)

    def getProduct(self, k: int) -> int:
        if k > len(self._products):
            return 0
        idx = -(k + 1)
        if abs(idx) > len(self._products):
            return self._products[-1]
        return self._products[-1] // self._products[idx]
    
if __name__ == "__main__":
    pon = ProductOfNumbers()
    pon.add(3)
    pon.add(0)
    pon.add(2)
    pon.add(5)
    pon.add(4)
    print(pon.getProduct(2)) # 20
    print(pon.getProduct(3)) # 40
    print(pon.getProduct(4)) # 0
    pon.add(8)
    print(pon.getProduct(2)) # 2