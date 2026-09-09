class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        storage = {}

        for num in nums:
            storage[num] = storage.get(num,0)+ 1
        
        sorted_nums = sorted(storage, key=storage.get, reverse=True)

        return sorted_nums[:k]
