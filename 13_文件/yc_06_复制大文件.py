# 1.打开文件
file_read = open("README")
file_write = open("README[复件]", "w")

# 2.读 写
while True:
    # 读取一行内容
    text = file_read.read()

    # 判断是否读取到内容
    if not text:
        break

    file_write.write(text)

# 3.关闭
file_read.close()
file_write.close()
