class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        stack = []
        for token in tokens:
            if token == "+":
                second = stack.pop()
                first = stack.pop()
                stack.append(first + second)
            elif token == "-":
                second = stack.pop()
                first = stack.pop()
                stack.append(first - second)
            elif token == "*":
                second = stack.pop()
                first = stack.pop()
                stack.append(first * second)
            elif token == "/":
                second = stack.pop()
                first = stack.pop()
                if (second > 0 and first > 0) or (second < 0 and first < 0):
                    stack.append(first // second)
                else:
                    stack.append(-1 * (abs(first) // abs(second)))
            else:
                stack.append(int(token))

        return stack[-1]

if __name__ == "__main__":
    s = Solution()
    tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]

    print(s.evalRPN(tokens))