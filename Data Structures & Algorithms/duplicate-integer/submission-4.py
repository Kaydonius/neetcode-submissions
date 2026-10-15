class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # # a set has no duplicates allowed.
        # check = set()
        # # iterate through array
        # for i in nums:
        #     if i in check:
        #         return True
        #     check.add(i)
        # return False

        # # sorting approach
        # sortedNums = sorted(nums)
        # for i in range(1, len(nums)):
        #     if nums[i] == nums[i - 1]:
        #         return True
        # return False

        # brute force approach
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] == nums[j]:
                    return True
        return False
