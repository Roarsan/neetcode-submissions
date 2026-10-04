class Solution:
    def minWindow(self, s: str, t: str) -> str:
        storage = {}
        window = {}

        # Count characters needed from t
        for char in t:
            storage[char] = storage.get(char, 0) + 1

        left = 0
        have = 0
        need = len(storage)

        minlength = float("inf")
        result = [-1, -1]

        for right in range(len(s)):
            char = s[right]
            window[char] = window.get(char, 0) + 1

            # This character now satisfies its requirement
            if char in storage and window[char] == storage[char]:
                have += 1

            # Current window contains everything we need
            while have == need:
                currentLength = right - left + 1

                # Save smallest valid window
                if currentLength < minlength:
                    minlength = currentLength
                    result = [left, right]

                # Remove left character
                leftChar = s[left]
                window[leftChar] -= 1

                # Did removing it break a requirement?
                if (
                    leftChar in storage
                    and window[leftChar] < storage[leftChar]
                ):
                    have -= 1

                left += 1

        left, right = result

        if minlength == float("inf"):
            return ""

        return s[left:right + 1]