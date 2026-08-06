class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        exists = set()
        for n in nums:
            if n not in exists:
                exists.add(n)
            else:
                return True
        return False