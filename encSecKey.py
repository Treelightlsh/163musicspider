import random


def random_charts(n):
    """
    从choices列表中随机生成n位字符串
    :param n:
    :return:
    """
    # 定义被选择的字符串
    choices = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    # 定义结果字符串
    c = ''
    for i in range(n):
        c += random.choice(choices)
    return c


def aes_parse(s):
    """
    对字串s进行解析
    :param s:
    :return:
    """
    l = []
    for i in range(len(s)):
        pass

if __name__ == '__main__':
    print(random_charts(16))