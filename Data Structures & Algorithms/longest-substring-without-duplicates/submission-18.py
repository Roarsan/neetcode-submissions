class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        storage = {}
        maxlength = 0
        left = 0
        for right in range(len(s)):
            currChar = s[right]
            storage[currChar] = storage.get(currChar,0)+1 
            while storage[currChar] > 1:
                storage[s[left]] -= 1
                left += 1

            windowlength = right - left + 1

            maxlength = max(windowlength,maxlength)

        return maxlength





        