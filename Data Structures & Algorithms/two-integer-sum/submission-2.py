class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        storage = {}
        for i in range(len(nums)):
            key = nums[i]
            

            diff = target - key

            if diff in storage:
                return [storage[diff],i]
            storage[key] = i
        return null

        