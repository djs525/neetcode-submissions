class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        #whenever we have something where duplicates are concerned
        #use a set
        duplicate = set()

        for i in range(len(nums)):
            if nums[i] in duplicate:
                return True
            duplicate.add(nums[i])
        return False