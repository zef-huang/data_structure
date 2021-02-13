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


if __name__ == '__main__':
    base_n = transfer_to_8_base(159)
    print(base_n)