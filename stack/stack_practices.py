# coding=utf8


# ------------------------------------------------------
# 1. 使用栈实现 8 进制转换
# ------------------------------------------------------

stack = []


def transfer_to_8_base(number):
    while number:
        remainder = number % 8
        if remainder:
            stack.append(remainder)
        else:
            break
        number /= 8

    base_n = 0
    while stack:
        base_n *= 10
        n = stack.pop()
        base_n += n

    return base_n



# ------------------------------------------------------
# 2. 使用栈实现括号匹配是否有效
# [(())][]
# ------------------------------------------------------

def is_branket_match(express):
    stack = []
    for branket in express:
        if branket == '(' or branket == '[':
            stack.append(branket)
        elif branket == ')' and stack:
            if stack and '(' == stack.pop():
                continue            
        elif branket == ']' and stack:
            if '[' == stack.pop():
                continue
        else:
            return False
    
    if stack:
        return False
    
    return True


if __name__ == '__main__':
    express = '[(())][]]'
    result = is_branket_match(express)
    print(result)