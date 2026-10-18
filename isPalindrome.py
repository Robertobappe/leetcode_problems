class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        L = []

        for i in range(len(s)):
            if s[i].isalnum():
                L.append(s[i])
        s = ''.join(L)

        return s == s[::-1]
        
