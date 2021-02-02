s = "((())()(())))"


def is_correct_parenthesis(string):
    arr_stack = []
    for i in string:
        if i == '(':
            arr_stack.append(i)
        else:
            if len(arr_stack) == 0 or arr_stack.pop() != '(':
                return False
    if len(arr_stack) == 0:
        return True
    else:
        return False



print(is_correct_parenthesis(s))  # False 를 반환해야 합니다!
