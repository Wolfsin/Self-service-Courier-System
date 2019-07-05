import random


def make(bit=6, alpha=False):
    number = ""
    # 通过for循环控制验证码位数
    for i in range(bit):
        # 生成随机数字0-9
        num = random.randint(0, 9)
        # 需要字母验证码,不用传参,如果不需要字母的,关键字 alpha = False
        if alpha:
            upper_alpha = chr(random.randint(65, 90))
            lower_alpha = chr(random.randint(97, 122))
            num = random.choice([num, upper_alpha, lower_alpha])
        number = number + str(num)
    return number

