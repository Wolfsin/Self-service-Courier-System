class User(object):
    """用户信息类，属性有：用户名、密码、手机号"""

    def __init__(self, username, password):
        # id为数据库自动生成
        self._user_id = None
        self._username = username
        self._password = password
        self._phone = None

    @property
    def user_id(self):
        return self._user_id

    @user_id.setter
    def user_id(self, id):
        self._user_id = id

    @property
    def username(self):
        return self._username

    @username.setter
    def username(self, name):
        self._username = name

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, psw):
        self._password = psw

    @property
    def phone(self):
        return self._phone

    @phone.setter
    def phone(self, number):
        self._phone = number


