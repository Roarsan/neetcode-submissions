class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        storage = {}

        for num in nums:

            key = num

            if num in storage:
                return True
            else:
                storage[key] = storage.get(num,0) + 1
        return False