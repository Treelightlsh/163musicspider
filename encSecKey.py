import random
import math


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


class AES_Parser(object):
    def __init__(self, s):
        self.sigBytes = 0
        self.words = []
        self.s = s
        self.aes_parse()

    def aes_parse(self):
        """
        对字串s进行解析
        :param s:
        :return:
        """
        # 计算结果列表长度
        res_l_length = math.ceil(len(self.s) / 4)
        # 定义结果列表
        res_l = []
        # 初始化结果列表的值均为0
        for i in range(res_l_length):
            res_l.append(0)
        for i in range(len(self.s)):
            res_l[i >> 2] |= (ord(self.s[i]) & 255) << 24 - 8 * (i % 4)
        self.words = res_l
        self.sigBytes = len(self.words) * 4




if __name__ == '__main__':
    aes_p1 = AES_Parser('0CoJUm6Qyw8W8jud')
    aes_p2 = AES_Parser('0102030405060708')
    print(aes_p2.sigBytes, aes_p2.words)
