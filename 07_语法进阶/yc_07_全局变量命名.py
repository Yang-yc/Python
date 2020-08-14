gl_num = 10
# 再定义一个全局变量
gl_title = "样衰衰"
# 在定义一个全局变量
gl_name = "杨帅帅"


def demo():
    # 如果局部变量的名字和全局变量的名字相同
    # pycharm会在局部变量下方显示一个灰色的虚线
    gl_num = 99
    print("%d" % gl_num)
    print("%s" % gl_title)
    print("%s" % gl_name)


demo()
