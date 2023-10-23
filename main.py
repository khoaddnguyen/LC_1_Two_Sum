# Input:
#  Array of integer nums = [2, 7, 11, 15]
#  target = 9
# Output: [0, 1]


def twoSum(self, nums: List[int], target: int) -> List[int]:
    prevMap = {}  # val : index

    for i, n in enumerate(nums):
        diff = target - n
        if diff in prevMap:
            return[prevMap[diff], i]
        prevMap[n] = i
    return
