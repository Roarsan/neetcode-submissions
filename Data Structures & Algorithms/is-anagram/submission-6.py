class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        storage1 = {}
        storage2 = {}

        for char in s:
            key = char

            storage1[key] = storage1.get(char,0)+ 1
        for char in t:
                key = char

                storage2[key] = storage2.get(char,0)+ 1   
        if storage1 == storage2:
            return True
        else:
            return False 