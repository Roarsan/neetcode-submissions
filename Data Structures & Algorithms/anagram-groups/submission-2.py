class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = []
        storage = {}

        for word in strs:
            key = "".join(sorted(word))
            if key not in storage:
                storage[key] = []
            storage[key].append(word)
        return list(storage.values())