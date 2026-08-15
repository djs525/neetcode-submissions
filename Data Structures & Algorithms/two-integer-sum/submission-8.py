class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        # need a hashMap to store the values for O(1) lookup
        hashMap = {} # num : index

        # populating the hashMap
        for i, n in enumerate(nums):
            hashMap[n] = i
        
        # traversing the array now
        # we will take the current element
        # check whether target - curElement exists in hashMap
        # if yes, append the 2 indices to a result array
        # return sorted(res) : smaller index first

        res = []
        for i in range(len(nums)):
            diff = target - nums[i]
            # make sure that both indices are unique
            if diff in hashMap and hashMap[diff] != i:
                res.append(hashMap[diff])
                res.append(i)
                break
        
        return sorted(res)