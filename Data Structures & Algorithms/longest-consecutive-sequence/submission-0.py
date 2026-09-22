class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        storage = set(nums)

        longest = 0
        for num in nums:
            if num - 1 not in storage:
                current = num
                count = 1 
                while  current+1 in storage:
                    current += 1
                    count += 1
                longest = max(count,longest)
        return longest