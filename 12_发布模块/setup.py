from distutils.core import setup

setup(name="yc.message",  # 包名
      version="1.0",  # 版本
      description="ycc`s 发送和接受信息模块",  # 描述信息
      long_description="完整的发送和接受信息模块",  # 完整描述信息
      author="ycc",  # 作者
      author_email="ycc20121404@163.com",  #作者邮箱
      url="主页（木有几）",  # 主页
      py_modules=["yc_message.send_message",
                  "yc_message.receive_message"])
