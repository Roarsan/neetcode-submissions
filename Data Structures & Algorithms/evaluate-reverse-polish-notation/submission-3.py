class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for token in tokens:
            if token not in ["+", "-", "*", "/"]:
                stack.append(int(token))
            else:
                num1 = stack.pop()
                num2 = stack.pop()

                if token == "-":
                    res = num2 - num1

                elif token == "+":
                    res = num1+num2

                elif token == "*":
                    res = num1 * num2

                else:
                    res = int(num2 / num1)

                stack.append(res)
        return int(stack[-1])