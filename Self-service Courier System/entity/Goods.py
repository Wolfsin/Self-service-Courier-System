class Goods(object):
    """快递物品类，属性有：快递单号、收货手机、货柜号、提货号"""

    def __init__(self, express_number):
        # id为数据库自动生成
        self._goods_id = None
        self._express_number = express_number
        self._phone = None
        self._container_number = None
        self._pick_up_code = None

    @property
    def goods_id(self):
        return self._goods_id

    @goods_id.setter
    def goods_id(self, id):
        self._goods_id = id

    @property
    def express_number(self):
        return self._express_number

    @express_number.setter
    def express_number(self, number):
        self._express_number = number

    @property
    def phone(self):
        return self._phone

    @phone.setter
    def phone(self, number):
        self._phone = number

    @property
    def container_number(self):
        return self._container_number

    @ container_number.setter
    def container_number(self, number):
        self._container_number = number

    @property
    def pick_up_code(self):
        return self._pick_up_code

    @pick_up_code.setter
    def pick_up_code(self, number):
        self._pick_up_code = number
