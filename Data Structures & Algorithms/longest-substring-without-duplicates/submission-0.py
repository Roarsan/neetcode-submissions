class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0 
        storage = set()
        maxLength = 0

        for i in range(len(s)):
            currentNum = s[i]

            while currentNum in storage:
                storage.remove(s[left])
                left +=1
            storage.add(currentNum)

            maxLength = max(maxLength,i-left+1)
        return maxLength

            


        