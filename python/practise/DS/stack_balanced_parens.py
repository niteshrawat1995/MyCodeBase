# Determine whether parenthesis are balanced using stack.
from Stack import Stack


def is_paren_balanced(paren_string):
    s = Stack()
    is_balanced = True
    index = 0
    while index < len(paren_string) and is_balanced:
        paren = paren_string[index]
        if paren in '[{(':
            s.push(paren)
        else:
            # if the first element is a closing parenthesis, we return by checking if the stack is empty or not.
            if s.is_empty():
                is_balanced = False
            # pop the top closed parenthesis and check if it matches the current parenthesis.
            else:
                top = s.pop
                if not is_matched(top, paren):
                    is_balanced = False
            index += 1
    if is_balanced and s.is_empty():
        return True
    return False


def is_matched(open, close):
    if open == '[' and close == ']':
        return True
    if open == '{' and close == '}':
        return True
    if open == '(' and close == ')':
        return True
    else:
        return False

# Driver


paren_string = '[{}]'
print(is_paren_balanced(paren_string))
