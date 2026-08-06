class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        res = []

        for num in nums:
            count[num] = 1 + count.get(num, 0)
        
        for i in range(k):
            max_key = max(count, key=count.get)
            res.append(max_key)
            count[max_key] = -1

        return res

        

        

        


        







