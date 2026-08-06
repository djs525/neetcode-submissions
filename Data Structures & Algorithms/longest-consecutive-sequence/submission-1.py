class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashset = set(nums)
        longest = 0

        for num in nums:
            length = 1
            while num - 1 in hashset:
                length += 1
                num = num - 1
            longest = max(length, longest)
        
        return longest

