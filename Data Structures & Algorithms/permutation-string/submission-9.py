class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        storage = {}
        storage2 = {}
        left = 0

        for right in range(len(s1)):
            char = s1[right]
            storage[char] = storage.get(char,0)+1

        for right in range(len(s2)):
            char = s2[right]
            storage2[char] = storage2.get(char,0)+1

            while right - left + 1 > len(s1):
                storage2[s2[left]] -= 1

                if storage2[s2[left]] == 0:
                    del storage2[s2[left]]
                left += 1

            
            if storage == storage2:
                return True
        return False



        