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
            total += nums[i]
            # with i again
            dfs(total, cur, i)
            cur.pop()
            total -= nums[i]
        
            # without
            dfs(total, cur, i + 1)

        dfs(0, [], 0)
        return res


