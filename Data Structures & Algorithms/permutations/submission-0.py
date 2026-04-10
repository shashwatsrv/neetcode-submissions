class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n=len(nums)
        res,sol=[],[]

        def backtrack():
            if len(sol)==n:
                res.append(sol[:])
                return
            
            for i in range(n):
                if nums[i] not in sol:
                    sol.append(nums[i])
                    backtrack()
                    sol.pop()
        backtrack()
        return res
