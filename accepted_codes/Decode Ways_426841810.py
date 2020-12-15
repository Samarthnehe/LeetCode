from functools import lru_cache
class Solution:
    def numDecodings(self, s: str) -> int:
        if not s:
            return 0
        @lru_cache(maxsize=None)
        def find(s):
            if not s:
                return 1
            temp=0
            if(0<int(s[0])<=9):
                temp+=find(s[1:])
            if(10<=int(s[:2])<=26):
                temp+=find(s[2:])
            return temp
        return find(s)
            
