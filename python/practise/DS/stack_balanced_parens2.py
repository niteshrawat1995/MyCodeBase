from Stack import Stack
#The day sublime quit on me :(

def is_parens_balanced(paren_string):
    index =0
    is_balanced =True
    s = Stack()

    while index< len(paren_string) and is_balanced:
        paren = paren_string[index]

        if paren in '[{(':
            s.push(paren)
        else:
            if s.is_empty():
                is_balanced =False
            else:
                top = s.pop()
                if is_matched(top,paren) == False:
                    is_balanced = False
        index +=1
    if is_balanced and s.is_empty():
        return True
    else:
        return False

def is_matched(open_paren,close_paren):
    if open_paren=='[' and close_paren==']':
        return True
    if open_paren=='{' and close_paren=='}':
        return True
    if open_paren=='(' and close_paren==')':
        return True
    else:
        return False

input_str = '[{(})]'
print(is_parens_balanced(input_str))
    
                
                
