class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l=[]
        max_count=0
        if s==" " or len(s)==1:
            return 1
        for i in range(len(s)-1):
            l.append(s[i])
            for j in range(i+1,len(s)):
                if s[j] not in l:
                    l.append(s[j])
                else:
                    if(len(l)>max_count):
                        max_count=len(l)
                    break
            if(len(l)>max_count):
                max_count=len(l)
            l=[]
        return max_count
