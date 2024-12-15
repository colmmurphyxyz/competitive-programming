class MaxHeap:
    def __init__(self, elems: list[list[int]]):
        self._heap: list[tuple[int]] = list(map(
            lambda c: (self.key(c), c[0], c[1]),
            elems
        ))
        for i in range(len(self._heap)):
            self._bubble_up(i)

    def items(self) -> list[tuple[int]]:
        return list(map(lambda x: (x[1], x[2]), self._heap))

    def insert(self, item: tuple[int]):
        key = self.key(item)
        self._heap.append((key, item[0], item[1]))
        self._bubble_up(len(self._heap) - 1)

    def peek(self) -> tuple[int]:
        _, passes, total = self._heap[0]
        return (passes, total)

    def update_max(self, new_value: tuple[int]):
        key = self.key(new_value)
        self._heap[0] = (key, new_value[0], new_value[1])
        self._bubble_down(0)

    def key(self, item) -> float:
        if item is None:
            return -1
        if isinstance(item, int):
            return self._heap[item][0]
        elif isinstance(item, (tuple, list)):
            p, t = item[0], item[1]
            return (t - p) / (t * (t + 1))
        else:
            print("Bad parameter to key()")

    def _bubble_up(self, idx: int):
        if idx == 0:
            return
        parent_idx: int = self._parent(idx)
        if self.key(parent_idx) < self.key(idx):
            self._heap[parent_idx], self._heap[idx] = self._heap[idx], self._heap[parent_idx]
            self._bubble_up(parent_idx)

    def _bubble_down(self, idx: int):
        left_idx: int = None if self._left(idx) >= len(self._heap) else self._left(idx)
        right_idx: int = None if self._right(idx) >= len(self._heap) else self._right(idx)
        if left_idx is None and right_idx is None:
            return
        max_idx = max(left_idx, right_idx, key=self.key)
        if self.key(max_idx) < self.key(idx):
            return
        self._heap[idx], self._heap[max_idx] = self._heap[max_idx], self._heap[idx]
        self._bubble_down(max_idx)

    def _parent(self, idx: int) -> int:
        return (idx - 1) // 2
    
    def _left(self, idx: int) -> int:
        return (2 * idx) + 1
    
    def _right(self, idx: int) -> int:
        return (2 * idx) + 2

class Solution:
    def _average_pass_ratio(self, classes: list[list[int]]) -> float:
        pass_rates = list(map(lambda c: c[0] / c[1], classes))
        return sum(pass_rates) / len(pass_rates)

    def maxAverageRatio(self, classes, extraStudents: int) -> float:
        max_heap: MaxHeap = MaxHeap(classes)
        # for c in classes:
        #     max_heap.insert((c[0], c[1]))

        for _ in range(extraStudents):
            passes, total = max_heap.peek()
            max_heap.update_max((passes + 1, total + 1))

        return self._average_pass_ratio(max_heap.items())
    
if __name__ == "__main__":
    s = Solution()
    print(s.maxAverageRatio([[1,2],[3,5],[2,2]], 2))
    print(s.maxAverageRatio([[2,4],[3,9],[4,5],[2,10]], 4))
    print(s.maxAverageRatio(
        [[684,883],[254,259],[66,797],[699,987],[458,828],[441,563],[257,555],[450,872],[465,551],[12,406],[347,857],[176,265],[25,498],[662,813],[427,956],[585,1000],[20,64],[364,709],[142,594],[129,608],[142,266],[284,849],[408,578],[177,411],[92,628],[240,498],[8,182],[325,542],[513,915],[665,943],[449,953],[655,703],[232,749],[245,321],[507,704],[491,980],[231,730],[346,423],[574,626],[746,929],[670,940],[282,996],[225,662],[50,944],[74,782],[524,661],[378,899],[164,524],[785,812],[209,905],[306,320],[307,710],[566,870],[170,381],[719,719],[476,755],[88,609],[127,877],[621,919],[527,984],[387,585],[160,181],[257,437],[223,965],[584,737],[776,802],[54,507],[404,698],[653,735],[357,394],[528,866],[169,558],[42,748],[93,537],[262,828],[104,644],[274,755],[86,935],[983,999],[143,993],[632,795],[863,991],[676,704],[84,718],[456,872],[247,947],[872,995],[392,963],[822,926],[407,444],[169,932],[334,449],[130,638],[500,931],[218,983]],
        5976
    ))
