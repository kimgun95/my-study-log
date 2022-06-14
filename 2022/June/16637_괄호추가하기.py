n = int(input())
formula = input()
answer = float('inf') * -1 # 초기값을 0으로 설정하면 안됨. 음수까지 고려.

def bracket_operation(f): # 괄호가 존재하는 식 계산
    if f[1] == '+':
        return int(f[0]) + int(f[2])
    elif f[1] == '-':
        return int(f[0]) - int(f[2])
    elif f[1] == '*':
        return int(f[0]) * int(f[2])

def normal_operation(a, b, op): # 일반 계산
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b

def calculate(form): # 만든 식을 계산한다
    global answer
    length = len(form)
    i = 2
    num = int(form[0])
    oper = form[1]
    # 괄호 부터 계산
    while i < length:
        if form[i] == '(':
            res = bracket_operation(form[i+1:i+4])
            num = normal_operation(num, res, oper)
            if i + 5 < length:
                oper = form[i+5]
            i += 6
        else: # 그냥 숫자
            num = normal_operation(num, int(form[i]), oper)
            if i + 1 < length:
                oper = form[i+1]
            i += 2
    answer = max(answer, num)


def make_formula(idx, new_formula): # 모든 경우의 식을 만든다
    if idx >= n - 2:
        calculate(new_formula + formula[idx:])
        return
    if formula[idx] == '+' or formula[idx] == '-' or formula[idx] == '*':
        new_formula += formula[idx]
        idx += 1
    if idx != 0:
        make_formula(idx + 3, new_formula + '(' + formula[idx:idx+3] + ')')
    make_formula(idx + 1, new_formula + formula[idx])

if n == 1:
    answer = int(formula)
else:
    make_formula(0, "")
print(answer)