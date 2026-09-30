class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        res = []

        def dfs(total, cur, i):
            if i >= len(nums) or total > target:
                return
            if total == target:
                res.append(cur.copy())
                return

            
            cur.append(nums[i])
            # with i again
            dfs(total + nums[i], cur, i)
            cur.pop()
        
            # without
            dfs(total, cur, i + 1)

        dfs(0, [], 0)
        return res


