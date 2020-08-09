def print_lin(char, times):
    """打印单行分割线

    :param char: 分割字符
    :param times: 分割线重复的次数
    """
    print(char * times)


def print_lines(char, times):
    """打印多行分割线

    :param char: 分割线使用的分割字符
    :param times: 分割线重复的次数
    """
    row = 0
    while row < 5:
        print_lin(char, times)
        row += 1


print_lines("+", 50)
