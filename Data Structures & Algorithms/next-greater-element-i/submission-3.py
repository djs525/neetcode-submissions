class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        res = [-1] * len(nums1)

        # Need a hashMap that carries nums1 : index for easy lookup
        hashMap = {}
        for i, n in enumerate(nums1):
            hashMap[n] = i
        
        stk = []
        for i in range(len(nums2)):
            cur = nums2[i]
            while stk and i > 0 and cur >= stk[-1]:
                val = stk.pop()
                res[hashMap[val]] = cur

            if cur in hashMap:
                stk.append(cur)
        return res
