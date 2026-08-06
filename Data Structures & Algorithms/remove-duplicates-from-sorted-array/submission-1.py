class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l = 0
        r = 1

        while r != len(nums):
            if nums[l] == nums[r]:
                nums.remove(nums[l])
            else:
                l += 1
                r += 1
        return len(nums)