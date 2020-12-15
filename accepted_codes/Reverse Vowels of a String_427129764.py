class Solution:
    def reverseVowels(self, s: str) -> str:
        a=['a','e','i','o','u','A','E','I','O','U']
        stack=[]
        vowel=[]
        s=list(s)
        for i in range(len(s)):
            if(s[i] in a):
                stack.append(i)
                vowel.append(s[i])
        k=0
        vowel=vowel[::-1]
        for i in range(len(s)):
            if(s[i] in a):
                s[i]=vowel[k]
                k+=1
        return ''.join(s)
            
