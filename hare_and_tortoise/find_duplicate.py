import sys
from typing import List 


def find_duplicate(nums: List[str]):
    """ Find duplicate in list
    @param nums: list of length n with integers 1, .., n-1. 
        Where one and only one of the integers appear several times. 
    @return: the repeated number.
    """
    # Treat nums as a linked list where the values points to next element in list.
    # Then use Loyds tortoise and hare algorithm to find a loop.

    # If there is a loop then the tortoise and the hare will meet.
    tortoise = nums[0]
    hare = nums[nums[0]]
    while not tortoise == hare: #todo index error?
        tortoise = nums[tortoise]
        hare = nums[nums[hare]]
    
    # The remainder of the loop from the hares position is the same length 
    # as x mod L, where x is the distance from start to the entry point of the loop.
    hare = 0
    while not tortoise == hare:
        tortoise = nums[tortoise]
        hare = nums[hare]
    return tortoise
    

if __name__ == '__main__':
    print(find_duplicate([int(i) for i in sys.argv[1:]]))


