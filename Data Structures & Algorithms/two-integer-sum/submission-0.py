class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        res = []

        for i in range(len(nums)):
            first = nums[i]
            diff = target - first
            for j in range(i, len(nums)):
                if nums[j] == diff and j != i:
                    res.append(i)
                    res.append(j)
                    

        return res

