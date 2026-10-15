class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # a set has no duplicates allowed.
        check = set()
        # iterate through array
        for i in nums:
            if i in check:
                return True
            check.add(i)
        return False