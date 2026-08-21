class Solution:
    def isValid(self, s: str) -> bool:
        stk = []
        for char in s:
            if char == '[' or char == '(' or char == '{':
                stk.append(char)
            else:
                if not stk:
                    return False
                pop_item = stk.pop()
                is_not_closing_bracket = char == ']' and pop_item != '['
                is_not_closing_parentheses = char == ')' and pop_item != '('
                is_not_closing_angle_bracket = char == '}' and pop_item != '{'
                if is_not_closing_bracket or is_not_closing_parentheses or is_not_closing_angle_bracket:
                    return False
        return len(stk) == 0