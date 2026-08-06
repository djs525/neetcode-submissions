class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}

        #bucket sort
        freq = [[] for _ in range(len(nums) + 1)]
        res = []

        #populate the hashmap
        for num in nums:
            count[num] = 1 + count.get(num, 0)
        
        #populate the buckets
        # example: index = 4 which means the count of those elements
        # in nums
        # if at index = 4, we get [2,3] that means 'nums' has 4 2s and 4 3s
        # in the list
        for key, val in count.items():
            freq[val].append(key)
        
        # we start from the last position (highest freq)
        # check for elements with the highest count
        # append that to res
        # return res when its length matches k
        for i in range(len(nums), 0, -1):
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res
        

        


        







