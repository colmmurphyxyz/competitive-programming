class Solution:
    def _bubble_up(self, nums: list[int], i: int) -> None:
        if i == 0: return
        parent = (i - 1) // 2
        if nums[i] >= nums[parent]:
            nums[i], nums[parent] = nums[parent], nums[i]
            self._bubble_up(nums, parent)

    def _bubble_down(self, nums: list[int], i: int, heap_size: int) -> None:
        if i + 1 >= heap_size:
            return
        if i * 2 + 2 > heap_size:   # if no left child
            return
        if i * 2 + 3 > heap_size:   # if no right child
            max_child_idx = i * 2 + 1
        else:
            left_child = nums[i * 2 + 1]
            right_child = nums[i * 2 + 2]
            if left_child > right_child:
                max_child_idx = i * 2 + 1
            else:
                max_child_idx = i * 2 + 2
        if nums[max_child_idx] > nums[i]:
            nums[max_child_idx], nums[i] = nums[i], nums[max_child_idx]
            self._bubble_down(nums, max_child_idx, heap_size)

    def sortArray(self, nums: list[int]) -> list[int]:
        # max-heapify nums
        for i in range(1, len(nums)):
            self._bubble_up(nums, i)
        heap_size = len(nums)
        while heap_size > 0:
            # swap first and last elements of heap
            nums[0], nums[heap_size - 1] = nums[heap_size - 1], nums[0]
            heap_size -= 1
            self._bubble_down(nums, 0, heap_size)
        return nums


if __name__ == "__main__":
    s = Solution()
    print(s.sortArray([5, 1, 1, 2, 0, 0]))
    print(s.sortArray([5, 2, 3, 1]))
    print(s.sortArray([-2,2,2,8,10,10,11,12,13,14,16,55,21]))