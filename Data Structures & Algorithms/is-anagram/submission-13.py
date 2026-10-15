class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # return sorted(s) == sorted(t)

        # we can do better (O(n) space complexity)

        # base case to eliminate items off rip
        if len(s) != len(t):
            return False
        
        # since we don't need the order, we just need to make sure the same characters happen the same number of times
        
       
        s_count = {}
        t_count = {}

        for i in s:
            if i in s_count:
                s_count[i] += 1
            else:
                s_count[i] = 1
        
        for j in t:
            if j in t_count:
                t_count[j] += 1
            else:
                t_count[j] = 1
        
        return s_count == t_count


        

