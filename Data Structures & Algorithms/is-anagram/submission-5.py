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
        # return sorted(s) == sorted(t)
        
        # hashmap solution
        # lets have 2 hashmaps: 1 for each string
        # key = char, val = count
        # check for same length so we only have to iterate through one hashmap
        # and compare it to the other
        if len(s) != len(t):
            return False
        # these are the two hashmaps
        hashS = {}
        hashT = {}
        # use range(len) here bc we are about indices and the character its attached to
        for i in range(len(s)):
        # take the character at given index
        # use the get function so we don't get key error
        # get takes two parameters: required keyname and optional value. default is None
            hashS[s[i]] = 1 + hashS.get(s[i], 0)
            hashT[t[i]] = 1 + hashT.get(t[i], 0)
        # now make sure the hashmaps are the same
        # now we just want to compare the values, so no need for range(len)
        for c in hashS:
            if hashS[c] != hashT.get(c):
                return False
        return True

  

