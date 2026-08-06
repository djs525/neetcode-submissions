class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        #initialize 2 pointers, left and right
        left = 0
        right = len(numbers) - 1
        res = []

        while left < right:
            if numbers[left] + numbers[right] < target:
                left += 1
            
            elif numbers[left] + numbers[right] > target:
                right -= 1
            else:
                res.append(left+1)
                res.append(right+1)
                break
        
        return res

