# and/or/not

# 案例1 : 要求年龄 >= 20 并且性别为男, 可以参加非常勿扰
# age = 20
# sex = '男'
# if age >= 20 and sex == '男':
#     print('欢迎来到, 非常勿扰!')  # 只有两个条件同时满足, 才会执行此句代码

# 案例2 : 定义两门科目的分数(linux和mysql), 只要其中一门分数 > 60 就算及格
# linux_score = 50
# mysql_score = 65
# if linux_score > 60 or mysql_score > 60:
#     print('恭喜你, 考试通过')  # 任意条件满足都会执行
# else:
#     print('拜拜吧, 重考去吧')  # 条件都不满足才会执行

# 案例3: 定义一个布尔类型变量值代表员工, 判断是否是本公司员工, 不是本公司员工不许进入
man = False
if not man:  # not 是对条件取反(注意: 观察此条件时, 先不要带入man的值, 只看条件本身)
    print('非公勿入')  # 条件满足时执行
