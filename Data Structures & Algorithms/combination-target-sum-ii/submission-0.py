class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        n = len(candidates)
        candidates.sort()
        def solve(idx, path, currSum): 
            if currSum == target:
                res.append(path.copy())
                return 
            
            for i in range(idx, n):
                if i > idx and candidates[i] == candidates[i - 1]:
                    continue
                if currSum + candidates[i] > target:
                    break
                
                path.append(candidates[i])
                solve(i + 1, path, currSum + candidates[i])
                path.pop()
        
        solve(0, [], 0)
        return res