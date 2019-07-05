# coding=utf-8
import urllib
import urllib.request
import hashlib


# MD5加密接口密码
def md5(psw):
    m = hashlib.md5()
    m.update(psw.encode("utf8"))
    return m.hexdigest()


def send(phone, express_number, position_code, pickup_code):
    """
        the_page:
        '0': '短信发送成功',
        '41': '余额不足',
        '42': '账户已过期',
        '43': 'IP地址限制',
        '50': '内容含有敏感词'
    """
    # statusStr = {
    #     '0': '短信发送成功',
    #     '41': '余额不足',
    #     '42': '账户已过期',
    #     '43': 'IP地址限制',
    #     '50': '内容含有敏感词'
    # }
    smsapi = "http://api.smsbao.com/"
    # 短信平台账号
    user = 'user'
    # 短信平台密码
    password = md5('password')
    # 要发送的短信内容
    template = '【科院快递中心】您的快递单号 %s 已到达校快递中心（校图书馆对面），货柜号 %s ，取件码 %s 为了您快件的安全，请不要把提货码泄露给其他人。'
    parm = (express_number, position_code, pickup_code)
    content = template % parm
    # 开始发送
    data = urllib.parse.urlencode({'u': user, 'p': password, 'm': phone, 'c': content})
    send_url = smsapi + 'sms?' + data
    response = urllib.request.urlopen(send_url)
    the_page = response.read().decode('utf-8')
    # print(statusStr[the_page])
    # print(the_page)
    return the_page

