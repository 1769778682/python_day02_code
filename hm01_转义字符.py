# print('你好')
# 注意: print() 函数在执行时, 默认附带换行效果(\n: 换行)
print('我是', end='\n')
# 示例: 打印古诗词
print('白日依山尽, \n 黄河入海流')
# print('朋友')
# 要求: 以下打印不换行
print('你好', end='')
print('我是', end='')
print('朋友')
# 其他转义字符: \t : 制表符(tab键)
# 会产生类似空格的效果, 可以连续使用多个
print('你好', end='\t\t')
print('我是', end='\t')
print('朋友')