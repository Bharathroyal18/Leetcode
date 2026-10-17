class Solution:
    def calPoints(self, ops: list[str]) -> int:
        stack = []
        for i in range(len(ops)):

            if ops[i] not in ("C", "D", "+"):
                stack.append(int(ops[i]))

            elif ops[i] == "C":
                stack.pop()

            elif ops[i] == "D":
                stack.append(stack[-1] * 2)

            elif ops[i] == "+":
                stack.append(stack[-1] + stack[-2])
                
        return sum(stack)

        # stack = []
        # for i in range(len(ops)):

        #     if ops[i] == "C":
        #         stack.pop()
        #     elif ops[i] == "D":
        #         stack.append(stack[-1] * 2)
        #     elif ops[i] == "+":
        #         stack.append(stack[-1] + stack[-2])
        #     else:
        #         stack.append(int(ops[i]))
        # return sum(stack)


    