class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for i in range(len(tokens)-1, -1, -1):
            stack.append(tokens[i])

        values = []
        while stack:
            val = stack.pop()
            if val.lstrip('-').isdigit():
                values.append(int(val))
            else:
                first = values[-2]
                second = values[-1]
                values.pop()
                values.pop()
                if val == '-':
                    values.append(first - second)
                elif val == '+':
                    values.append(first + second)
                elif val == '*':
                    values.append(first * second)
                elif val == '/':
                    values.append(int(first / second))
                print(val)
            print(values)
        
        return values[0]