def sum_number(num):
    # 1.出口
    if num == 1:
        return 1
    # 2.数字的累加 num+(1...num-1)
    # 假设 _sum_number 能够正确处理1...num-1
    temp = sum_number(num - 1)
    return num + temp


result = sum_number(100)
print(result)