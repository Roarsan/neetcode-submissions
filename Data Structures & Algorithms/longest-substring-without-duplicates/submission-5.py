class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxlength = 0
        left = 0
        currentLength = 0
        storage = set()
        for current in range(len(s)):
            currentLetter = s[current]

            while currentLetter in storage:
                storage.remove(s[left])
            
                left +=1

            storage.add(currentLetter)

            currentlength = current - left + 1

            maxlength = max(currentlength,maxlength)
        return maxlength
        