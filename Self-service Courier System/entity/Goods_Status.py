from entity.Goods import Goods


class GoodsStatus (Goods):
    """快递物品状态类，继承快递物品类，新增 是否已发送短信标记 和 是否完成收货标记"""

    def __init__(self, express_number):
        super().__init__(express_number)
        # status_id为数据库自动生成
        self._status_id = None
        self._is_send_message = False
        self._is_pick_up = False

    @property
    def status_id(self):
        return self._status_id

    @status_id.setter
    def status_id(self, id):
        self._status_id = id

    @property
    def is_send_message(self):
        return self._is_send_message

    @is_send_message.setter
    def is_send_message(self, flag):
        self._is_send_message = flag

    @property
    def is_pick_up(self):
        return self._is_pick_up

    @is_pick_up.setter
    def is_pick_up(self, flag):
        self._is_pick_up = flag
