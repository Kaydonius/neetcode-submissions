class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # return sorted(s) == sorted(t)

        # we can do better (O(n) space complexity)

        # base case to eliminate items off rip
        if len(s) != len(t):
            return False
        
        # since we don't need the order, we just need to make sure the same characters happen the same number of times

        # for O(1) space, we can predefine size so we get a constant

        count = [0] * 26
        for i in range(len(s)):
            count[ord(s[i]) - ord('a')] += 1
            count[ord(t[i]) - ord('a')] -= 1

        for val in count:
            if val != 0:
                return False

        return True


        

