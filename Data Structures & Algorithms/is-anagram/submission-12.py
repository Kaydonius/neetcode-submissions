class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # return sorted(s) == sorted(t)

        # we can do better (O(n) space complexity)

        # base case to eliminate items off rip
        if len(s) != len(t):
            return False
        
        # since we don't need the order, we just need to make sure the same characters happen the same number of times
        
       
        countS, countT = {}, {}

        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)
        return countS == countT


        

