class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res,sol=[],[]
        n=len(candidates)

        def backtrack(start,total):
            if total==target:
                res.append(sol[:])
                return
            for i in range(start,n):
                if i>start and candidates[i]==candidates[i-1]:
                    continue
                if total+candidates[i]>target:
                    break

                sol.append(candidates[i])
                backtrack(i+1,total+candidates[i])     
                sol.pop()   
        backtrack(0,0)
        return res