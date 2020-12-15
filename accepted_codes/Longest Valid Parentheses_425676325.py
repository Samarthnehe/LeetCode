class Solution:
    def longestValidParentheses(self, s: str) -> int:
        if len(s) == 0:
            return 0
        
        heap = [-1]
        for i in range(len(s)):
            if len(heap) == 1:
                heap.append(i)
            else:
                if s[heap[-1]] == '(' and s[i] == ')':
                    heap.pop()
                else:
                    heap.append(i)
        heap.append(len(s))
        print(heap)
        res = []
        for i in range(1, len(heap)):
            res.append(heap[i] - heap[i - 1]-1 )
        
        return max(res)
