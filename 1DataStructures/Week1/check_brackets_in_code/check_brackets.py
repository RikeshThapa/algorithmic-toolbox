# python3

import sys

class Bracket:
    def __init__(self, bracket_type, position):
        self.bracket_type = bracket_type
        self.position = position

    def Match(self, c):
        if self.bracket_type == '[' and c == ']':
            return True
        if self.bracket_type == '{' and c == '}':
            return True
        if self.bracket_type == '(' and c == ')':
            return True
        return False

if __name__ == "__main__":
    text = sys.stdin.read()

    opening_brackets_stack = []
    success = 1
    for i, next in enumerate(text):
        if next == '(' or next == '[' or next == '{':
            opening_bracket_stack.append(next)

        if next == ')' or next == ']' or next == '}':
            bracket = Bracket(opening_bracket_stack.pop(), i-1)
            if bracket.Match(next):
                pass
            else:
                index = i
                success = 0
                break
                
    if success:
        print("Success")
    else:
        print(index)
