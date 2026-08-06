class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {} #Key: num, Value: count
        res = []
        for num in nums:
            if num in count:
                count[num] += 1
            else:
                count[num] = 1
        
        freq = [[] for i in range(len(nums) + 1)]

        for key,val in count.items():
            freq[val].append(key)
        

        for i in range(len(nums),0, -1):
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res







