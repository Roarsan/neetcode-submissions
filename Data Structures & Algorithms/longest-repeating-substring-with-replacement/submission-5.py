class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        storage ={}
        window = {}
        left = 0
        maxlength = 0
        for right in range(len(s)):
            currChar = s[right]

            storage[currChar] =  storage.get(currChar,0)+1

            maxfrequency = max(storage.values())
            currentlength = right - left + 1

            while currentlength - maxfrequency > k:
                storage[s[left]] -= 1
                left += 1
                
                maxfrequency = max(storage.values())
                currentlength = right - left + 1

            maxlength = max(maxlength, currentlength)

        return maxlength

        