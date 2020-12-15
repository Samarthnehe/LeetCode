class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        length = len(candidates)
        output = []
        def backtrack(index, res, curSum):
            nonlocal output
            if curSum == target:
                output.append(res.copy())
                return
                
            for i in range(index, length):
                if (curSum + candidates[i]) <= target:
                    res.append(candidates[i])
                    backtrack(i, res, curSum + candidates[i])
                    res.pop(-1)

        backtrack(0, [], 0)
        return output
