class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left  = 0
        storage = {}
        maxlength = 0
        for right in range(len(s)):
            currChar = s[right]
            storage[currChar] = storage.get(currChar,0)+1

            while (right - left + 1) - (max(storage.values())) > k:
                storage[s[left]]-=1
                left += 1

            maxlength = max(maxlength,right - left + 1)

        return maxlength