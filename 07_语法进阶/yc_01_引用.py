def test(num):
    print("在函数内部 %d 对应的内存地址是 %d" % (num, id(num)))
    pass
    # 定义一个字符串变量
    result = "hello"
    print("函数要返回数据的内存地址是 %d" % id(result))
    # 将字符串变量返回,返回的是数据的引用，而不是数据本身
    return result


# 1.定义一个数字的变量
a = 10
print("a变量保存数据的内存地址是 %d" % id(a))
# 2.调用test函数,本质上传递的是实参保存数据的引用
# 注意：如果函数有返回值，但是没有定义变量接受
# 程序不会报错，但是无法获得返回结果
r = test(a)
print("%s 的内容地址是 %d" % (r, id(r)))