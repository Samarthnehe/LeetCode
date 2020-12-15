class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        mx=s.split(" ")
        done=0
        for i in range(len(mx)-1,-1,-1):
            if(mx[i]!=''):
                done=1
                return len(mx[i])
                
        if(done==0):
            return 0
