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


# function to check if two Range objects overlap
# as it takes as input the Range object, if lists/tuples were initially
# available, porting them to Range objects would be simple
def overlaps(rng1: Range, rng2: Range) -> bool:
    # there are quite a few cases were the ranges are overlapping but only two
    # cases were there are not
    if rng1.right < rng2.left or rng2.right < rng1.left:
        return False
    else:
        return True

# function to keep getting a valid value for the ranges
def coord_input(point: str):
    while True:
        try:
            coord = int(input("Please enter coordinate of " + point + ": "))
        except ValueError:
            print("Sorry that wasn't valid")
            continue
        else:
            break
    return coord

# function for getting point from user and using the above methods to determine
# whether there is overlap
def line_input():
    x1 = coord_input("x1")
    x2 = coord_input("x2")
    y1 = coord_input("y1")
    y2 = coord_input("y2")

    rng1 = Range(x1, x2)
    rng2 = Range(y1, y2)

    if overlaps(rng1, rng2):
        print("The two ranges do overlap")
    else:
        print("The two ranges do not overlap")

    while True:
        ans = input("Would you like to keep using the tool? [y/n]: ")
        if ans == "Y" or ans == "y":
            break
        elif ans == "N" or ans == "n":
            raise ValueError('Tool completion')
        else:
            print("Sorry please reinput your answer!")

# exception catch incase user wants to end tool prematurely
def main():
    print("Press CTRL-C at any point to stop early!")
    try:
        while True:
            line_input()
    except (KeyboardInterrupt, ValueError):
         print("\nThank you for using the overlap tool.")

if __name__ == "__main__":
    main()
