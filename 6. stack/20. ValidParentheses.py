from typing import List

def isValid(s: str) -> bool:
    stack: List[int] = []

    for char in s:
        if char == '(' or char == '[' or char == '{':
            stack.append(char)
        else:
            if not stack:
                return False

            if char == ')':
                if stack.pop() != '(':
                    return False

            elif char == ']':
                if stack.pop() != '[':
                    return False
            else:
                if stack.pop() != '{':
                    return False

    return True




if __name__ == "__main__":
    s = "(]"
    print(isValid(s))

    s1 = "()[]{}"
    print(isValid(s1))