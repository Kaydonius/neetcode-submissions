class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # i is the index. n is the current number
        check = {}
        for i, n in enumerate(nums):
            diff = target - n
            if diff in check:
                return [check[diff], i]
            else:
                check[n] = i

            # revisit this