# 定义一个布尔变量is_employee，编写代码判断是否是本公司成员
is_employee = False

# 如果不是提示不允许入内
if not is_employee:
    print("非本公司员工，请勿入内")

# 在开发中，通常希望某个条件不满足时，执行一些代码，可以用是not
# 另外，如果需要拼接复杂的逻辑计算条件，同样也有可能使用到not