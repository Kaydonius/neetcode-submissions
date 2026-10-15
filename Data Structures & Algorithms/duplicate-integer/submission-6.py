class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # use set to check for duplicates
        # checks the set if a number is alrdy there
        # if we pass over a number in the list thats already
        # in the set, its a duplicate

        seen = set()
        for i in nums:
            if i in seen:
                return True
            seen.add(i)
        return False

                