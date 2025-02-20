class Solution:
    def readBinaryWatch(self, turnedOn: int) -> list[str]:
        ret = []
        possible_nums = []
        self.generate(possible_nums, on=turnedOn, bits_set=0, curr_candidate="")
        for ans in possible_nums:
            hours = int(ans, base=2) >> 6
            mins = int(ans, base=2) & 0b111111
            if hours > 11 or mins >= 60:
                continue
            ret.append(f"{hours}:{mins:02}")
        return ret


    def generate(self, res: list[str], on: int, bits_set: int = 0, curr_candidate = "") -> None:
        if len(curr_candidate) == 10 and bits_set == on:
            res.append(curr_candidate)
        if len(curr_candidate) > 10:
            return
        if bits_set > on:
            return
        self.generate(res, on, bits_set + 1, curr_candidate + "1")
        self.generate(res, on, bits_set, curr_candidate + "0")

if __name__ == "__main__":
    s = Solution()
    print(s.readBinaryWatch(0))
    print(s.readBinaryWatch(1))
    print(s.readBinaryWatch(2))
    print(s.readBinaryWatch(3))
    print(s.readBinaryWatch(4))
    print(s.readBinaryWatch(5))
    print(s.readBinaryWatch(6))
    print(s.readBinaryWatch(7))
    print(s.readBinaryWatch(8))
    print(s.readBinaryWatch(9))
    print(s.readBinaryWatch(10))
        