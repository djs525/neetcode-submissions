class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        catch_duplicate = set()
        for num in nums:
            if num not in catch_duplicate:
                catch_duplicate.add(num)
            else:
                return True
        return False