class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        storage ={}
        maxlength = 0 


        for right in range(len(s)):
            currChar = s[right]

            storage[currChar] = storage.get(currChar,0)+1

            while storage[currChar] > 1:
                storage[s[left]] -= 1
                left += 1
            currentlength = right - left + 1


            maxlength = max(currentlength,maxlength)


        return maxlength

        