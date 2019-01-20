# Even though we have lists and tuples which are usable in python, having a
# class will give more liberaty to expand and add more if need be later on
class Range:
    # left and right variables are needed initially
    def __init__(self, left: int, right: int):
        if left < right:
            self.left = left
            self.right = right
        else:                                   # make sure the left bound is
            self.left = right                   # smaller than the right
            self.right = left
        self.calc_len()

    def calc_len(self):
        self.len = self.right - self.left

    # could possibly add methods for changing the left and right boundaries
    # of the range rather than changing directly, then we can also recall
    # the calc_len()

# method to check if two Range objects overlap
# as it takes as input the Range object, if lists/tuples were initially
# available, porting them to Range objects would be simple
def overlaps(rng1: Range, rng2: Range) -> bool:
    # there are quite a few cases were the ranges are overlapping but only two
    # cases were there are not
    if rng1.right < rng2.left or rng2.right < rng1.left:
        return False
    else:
        return True

def main():
    rng1 = Range(6,6)
    rng2 = Range(6,8)

    print(overlaps(rng1, rng2))

if __name__ == "__main__":
    main()
