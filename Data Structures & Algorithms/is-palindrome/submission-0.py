class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        test = []
        for i in s:
            if i.isalnum():
                test.append(i)
        if test == test[::-1]:
            return True
        return False