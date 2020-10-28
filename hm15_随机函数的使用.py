# 1. 导包
import random

# 2. 调用随机数方法
# random.randint(起始值, 结束值)
# 随机在1-10之间取值
print(random.randint(1, 10))  # 在1-10直接每次运行随机出一个数值
# print(random.randint(10, 10))  # 每次都是10
# print(random.randint(10, 1))  # 此句传值错误, 起始值<结束值
