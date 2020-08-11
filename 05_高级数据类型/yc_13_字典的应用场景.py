# 使用多个键值对，存储描述一个物体的相关信息--描述更复杂的数据信息
# 将多个字典放在一个列表中，在=再进行遍历
card_list = [
    {"name": "张三",
     "qq": "123456",
     "phone": "110"},
    {"name": "李四",
     "qq": "654321",
     "phone": "10086"}
]

for card_info in card_list:
    print(card_info)