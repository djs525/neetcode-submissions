class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix = defaultdict(int)
        prefix[0] = 1  # prefix sum 0 occurs once before we start

        count = 0
        curr = 0

        for num in nums:
            curr += num  # prefix sum up to current index

            # how many previous prefix sums were curr - k?
            need = curr - k
            if need in prefix:
                count += prefix[need]

            # record this prefix sum
            prefix[curr] += 1

        return count