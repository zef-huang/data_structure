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



# ------------------------------------------------------
# 3. kmp 算法实现字符串模式匹配
# ------------------------------------------------------


def index_kmp(s, s_pattern):
    pass


def get_s_pattern_next(s):
    '''获取模式字符串的 next 前缀表
    '''
    
    j = 0
    max_len = len(s)

    # 初始化前缀表 next
    next = [1] * max_len
    next[0] = 0

    for i in range(1, max_len):
        while s[i] != s[j] and j>0:
            j = next[j - 1]

        if s[i] == s[j]:
            j += 1

        next[i] = j

    print(next)
    return next


def index_kmp(s, s_pattern):
    s_len = len(s)
    pattern_len = len(s_pattern)
    next_list = get_s_pattern_next(s_pattern)

    index = -1
    i = 0
    j = 0
    while i < s_len and j < pattern_len:
        if s[i] == s_pattern[j]:
            i += 1
            j += 1
        else:
            # j 回退
            j = next_list[j]
            if j:
                # 从 0 开始的字符串
                j -= 1
            else:
                i += 1

        if j == pattern_len - 1:
            index = i - pattern_len + 1

    return index
        

if __name__ == '__main__':
    s = 'abcaabbcabc'
    result = get_s_pattern_next(s)
    print(result)

    index = index_kmp('abcaabbcabc', 'aabb')
    print('index: %s' % index)
