class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # hashsetOne = set()
        # hashsetTwo = set()
        # for i in s:
        #     hashsetOne.add(i)
        # for j in t:
        #     hashsetTwo.add(j)
        # if hashsetOne == hashsetTwo:
        #     return True
        # return False
        # soln doesn't handle duplicates well

        # sorting solution
        return sorted(s) == sorted(t)

        
  

