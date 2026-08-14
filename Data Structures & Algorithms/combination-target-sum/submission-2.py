class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        # i -> marks the current index in the nums array
        # cur -> marks the elements we are using so far eg. [2,2,2] or [2,3,4] or [2,2,3,3,4] etc..
        # total -> marks the total of the elements within cur at the moment
        def dfs(i, cur, total):

            # knock off the base cases
            if total == target:
                res.append(cur.copy())
                return
            
            if i >= len(nums) or total > target:
                return
            
            # we are creating 2 branches, one where we add the same element
            # the other where we skip the element

            cur.append(nums[i])
            dfs(i, cur, total + nums[i])
            cur.pop()
            dfs(i+1, cur, total)
        
        dfs(0,[],0)
        return res