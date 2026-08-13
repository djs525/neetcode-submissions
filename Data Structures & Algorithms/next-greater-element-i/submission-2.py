class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        stk = []

        res = [-1] * len(nums1)
        nums1Idx = {n:i for i,n in enumerate(nums1)} #storing nums: index for easy lookup

        #traversing nums2
        for i in range(len(nums2)):
            cur = nums2[i]

            while stk and cur > stk[-1]:
                val = stk.pop()
                res[nums1Idx[val]] = cur
            # if after while because we want stack to be decreasing
            if cur in nums1Idx:
                stk.append(cur)
        
        return res
