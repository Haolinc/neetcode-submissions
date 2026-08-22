class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stk = []
        operations = {
            '+': lambda a, b: a + b,
            '-': lambda a, b: a - b,
            '*': lambda a, b: int(a * b),
            '/': lambda a, b: int(a / b),
        }
        for token in tokens:
            if token in operations:
                b = stk.pop()
                a = stk.pop()
                stk.append(operations[token](a, b))
            else:
                stk.append(int(token))
        print(stk)
        return stk.pop()