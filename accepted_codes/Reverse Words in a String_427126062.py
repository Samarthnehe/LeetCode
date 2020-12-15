class Solution:
    def reverseWords(self, s: str) -> str:
        l=s.split()
        l1=l[::-1]
        string=""
        for i in l1:
            string+=i
            string+=" "
        return string.strip()
