class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        storage1 = {}
        storage2 = {}

        for char in s:
            storage1[char] = storage1.get(char, 0) + 1

        for char in t:
            storage2[char] = storage2.get(char, 0) + 1
        
        return storage1 == storage2