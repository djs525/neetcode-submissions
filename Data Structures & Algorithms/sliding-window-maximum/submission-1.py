class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        
        # res = []
        # hashMap = {}

        # for i in range(k):
        #     hashMap[i] = nums[i]
        
        # res.append(max(hashMap.values()))

        # l = 0
        # for r in range(k,len(nums)):
        #     hashMap[r] = nums[r]
        #     del hashMap[l]
        #     l += 1

        #     res.append(max(hashMap.values()))
        
        # return res

        q = collections.deque() # monotic decreasing queue
        res = []
        l = r = 0

        while r < len(nums):
            while q and q[-1] < nums[r]:
                q.pop()
            q.append(nums[r])
            
            if (r >= k - 1):
                res.append(q[0])

                if nums[l] == q[0]:
                    q.popleft()
                l += 1

            r += 1
        return res




