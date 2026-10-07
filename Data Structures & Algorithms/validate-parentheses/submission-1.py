class Solution:
    def isValid(self, s: str) -> bool:
        stack =[]
        closingBracket ={
            ")":"(",
            "]":"[",
            "}":"{",
        }

        for char in s:

            if char in closingBracket:
                if stack and stack[-1] == closingBracket[char]:
                    stack.pop()
                else:
                    return False

            else:
                stack.append(char)
        return len(stack) == 0