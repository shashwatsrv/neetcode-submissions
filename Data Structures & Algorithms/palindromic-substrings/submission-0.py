class Solution:
    def countSubstrings(self, s: str) -> int:

        res = 0

        def pl(l,r):
            if l < 0 or r > len(s) - 1:
                return 0
            if s[l] == s[r]:
                return 1 + pl(l - 1, r + 1)
            return  0

        for i in range(len(s)):
            res += pl(i,i) + pl(i,i+1)
            
        return res