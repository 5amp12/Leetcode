class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = {"+", "/", "-", "*"}

        for token in tokens:
            if token not in operators:
                stack.append(int(token))
            else:
                b = stack.pop()
                a = stack.pop()
                if token == "/":
                    stack.append(int(a / b))
                elif token == "+":
                    stack.append(a + b)
                elif token == "-":
                    stack.append(a - b)
                else:
                    stack.append(a * b)
            # print(tokens)
                

        return stack[0]