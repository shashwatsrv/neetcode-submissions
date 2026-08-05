class Solution:
    def numDecodings(self, s: str) -> int:
        cache={}

        def dp(i):
            if i == len(s):
                return 1
            if s[i] == '0':
                return 0
            
            if i in cache:
                return cache[i]
            
            ways = dp(i+1)
            if ((i+1) < len(s) and 10 <= int(s[i:i+2]) <= 26) :
                ways += dp(i+2)
            
            cache[i] = ways
            return ways
        return dp(0)