class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        operations = {"+", "-", "*", "/"}
        stack = []

        for i in range(len(tokens)):
            if tokens[i] in operations:
                b = stack.pop()
                a = stack.pop()

                if tokens[i] == "+":
                    result = a + b
                elif tokens[i] == "-":
                    result = a - b
                elif tokens[i] == "*":
                    result = a * b
                else:
                    result = int(a / b)

                stack.append(result)
            else:
                stack.append(int(tokens[i]))

        return stack[0]        