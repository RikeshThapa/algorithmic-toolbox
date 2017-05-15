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
            bracket = Bracket(next, i+1)
            opening_brackets_stack.append(bracket)
            continue

        if next == ')' or next == ']' or next == '}':
            nextBracket = Bracket(next, i+1)
            if opening_brackets_stack!=[]:
                bracket = opening_brackets_stack.pop()
            elif i==0:
                success=0
                index=1
                break
            else:
                success=0
                index=nextBracket.position
                break
            
            if bracket.Match(nextBracket.bracket_type):
                continue
            else:
                index = nextBracket.position
                success = 0
                break
    #Final check to see if all brackets have been satisfied
    if success==0:
        print(index)
    elif opening_brackets_stack != []:
        mismatch = opening_brackets_stack.pop()
        print(mismatch.position)
    else:
        print("Success")
        
