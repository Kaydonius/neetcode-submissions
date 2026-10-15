class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # first, we need to recognize that we need to return indices.
        # next, we need a variable to compute what we're looking for.
        # if nums[i] + nums[j] == target, then target - nums[i] must be the difference
        # so we will have a diff variable.
        # for i in nums:
        #     diff = target - nums[i]
        # # we can probably use a hashmap to number off the indices we don't need.
        # check = {}
        # since we need to count the number of occurences, we can use enumerate
        # lets rework our order of operations

        check = {}
        for i, n in enumerate(nums):
            # where i is the index and n is the numbers
            diff = target - n
            # now we see if the difference (one of our good numebrs) is in the hashmap
            if diff in check:
                # return the indices of the 2 numbers that add up to the target
                return [check[diff], i]
            else:
                #if not, set the index where the number is to i
                check[n] = i
