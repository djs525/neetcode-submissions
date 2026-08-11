class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        hashMap = {}

        #populating the hashMap
        for i,n in enumerate(nums):
            if n in hashMap:
                if abs(i - hashMap[n]) <= k:
                    return True
            hashMap[n] = i
        return False