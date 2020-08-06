# 1、输入苹果的单价
price_str = input("苹果的单价:")
# 1、输入苹果的重量
weight_str = input("苹果的重量:")
# 3、计算支付的金额
# 注意：两个字符串变量之间是不能直接用乘法的
# money = price_str * weight_str
# 1>将价格转换为小数
price = float(price_str)
# 2>将重量转换为小数
weight = float(weight_str)
# 3>用两个小数来计算最终的金额
money = price * weight
print(money)