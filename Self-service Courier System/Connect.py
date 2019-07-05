import pymysql
from entity.Goods_Status import Goods, GoodsStatus
from ErrorMessageBox import show, show_fail_item


class DBController(object):

    def __init__(self):
        self.database = None

    def connectDB(self):
        try:
            self.database = pymysql.connect(
                host="127.0.0.1",
                port=3306,
                user="user",
                passwd="password",
                db="Self-service Courier System"
            )
            # self.database = pymysql.connect(
            #     host="127.0.0.1",
            #     port=3306,
            #     user="user",
            #     passwd="password",
            #     db="Test"
            # )
        except Exception as error:
            show(str(error))

    def find_user(self, username, password):
        self.connectDB()
        if self.database is None:
            return "had_error"
        else:
            cursor = self.database.cursor()
            sql = "SELECT count(1) FROM User WHERE username = %s AND password = %s"
            parm = (username, password)
            try:
                # 执行SQL语句
                cursor.execute(sql, parm)
                self.database.commit()
                # 获取第一条记录元组
                results = cursor.fetchone()
                if results[0]:
                    flag = True
                else:
                    # 没有找到记录
                    flag = False
            except Exception as error:
                self.database.rollback()
                show(str(error))
                return "had_error"
            finally:
                # 关闭数据库连接
                self.database.close()
            return flag

    def find_goods(self, express_number):
        self.connectDB()
        if self.database is None:
            return "had_error"
        else:
            cursor = self.database.cursor()
            sql = "SELECT goods_id FROM Goods_Information WHERE express_number = %s ORDER BY goods_id DESC"
            parm = express_number
            try:
                cursor.execute(sql, parm)
                self.database.commit()
                results = cursor.fetchone()
                if results:
                    goods_id = results[0]
                else:
                    # id为数据库自动生成，从1开始，0为空
                    goods_id = 0
            except Exception as error:
                self.database.rollback()
                show(str(error))
                return "had_error"
            finally:
                self.database.close()
            return goods_id

    def find_max_container_number(self):
        self.connectDB()
        if self.database is None:
            return "had_error"
        else:
            cursor = self.database.cursor()
            sql = "SELECT Max(container_number) FROM Goods_Information " \
                  "LEFT JOIN Goods_Status ON Goods_Information.goods_id = Goods_Status.goods_id" \
                  " WHERE is_pick_up = '0'"
            try:
                cursor.execute(sql)
                self.database.commit()
                results = cursor.fetchone()
                if results[0]:
                    max_container_number = results[0]
                else:
                    # id为数据库自动生成，从1开始，0为空
                    max_container_number = "000"
            except Exception as error:
                self.database.rollback()
                show(str(error))
                return "had_error"
            finally:
                self.database.close()
            return max_container_number

    def find_goods_status(self, goods_id, msg_or_pickup):
        self.connectDB()
        if self.database is None:
            return "had_error"
        else:
            cursor = self.database.cursor()
            msg_sql = "SELECT is_send_msg FROM Goods_Status WHERE goods_id = %s"
            pickup_sql = "SELECT is_pick_up FROM Goods_Status WHERE goods_id = %s"
            if "msg" is msg_or_pickup:
                sql = msg_sql
            else:
                sql = pickup_sql
            parm = goods_id
            try:
                cursor.execute(sql, parm)
                self.database.commit()
                results = cursor.fetchone()
                if results[0]:
                    flag = True
                else:
                    flag = False
            except Exception as error:
                self.database.rollback()
                show(str(error))
                return "had_error"
            finally:
                self.database.close()
            return flag

    def change_status(self, goods_id, msg_or_pickup, change_flag):
        self.connectDB()
        if self.database is None:
            return "had_error"
        else:
            cursor = self.database.cursor()
            msg_sql = "UPDATE Goods_Status SET is_send_msg = %s WHERE goods_id = %s"
            pickup_sql = "UPDATE Goods_Status SET is_pick_up = %s WHERE goods_id = %s"
            if "msg" is msg_or_pickup:
                sql = msg_sql
                operation_code = 1
            else:
                sql = pickup_sql
                operation_code = 2
            parm = (1 if change_flag else 0, goods_id)
            try:
                cursor.execute(sql, parm)
                self.database.commit()
                results = cursor.rowcount
                # 如果影响行数大于0
                if results:
                    flag = True
                    self.add_operation(goods_id, operation_code)
                else:
                    flag = False
            except Exception as error:
                self.database.rollback()
                show(str(error))
                return "had_error"
            finally:
                self.database.close()
            return flag

    def add_list_goods(self, goods_list: list):
        fail_item = []
        success_item = []
        for goods in goods_list:
            flag = self.add_goods(goods)
            if "had_error" is flag:
                fail_item.append(goods.express_number)
            elif flag:
                success_item.append(flag)
            else:
                fail_item.append(goods.express_number)
        if fail_item:
            show_fail_item(fail_item)
        else:
            return success_item

    def add_goods(self, goods: Goods):
        express_number = goods.express_number
        phone = goods.phone
        container_number = goods.container_number
        pick_uo_code = goods.pick_up_code
        self.connectDB()
        if self.database is None:
            return "had_error"
        else:
            cursor = self.database.cursor()
            information_sql = "INSERT INTO Goods_Information(express_number, phone, container_number, pick_up_code) "\
                              "values(%s, %s, %s, %s)"
            information_parm = (express_number, phone, container_number, pick_uo_code)
            status_sql = "INSERT INTO Goods_Status(goods_id, express_number) values(%s, %s)"
            try:
                cursor.execute(information_sql, information_parm)
                goods.goods_id = self.database.insert_id()
                if goods.goods_id:
                    status_parm = (goods.goods_id, express_number)
                    cursor.execute(status_sql, status_parm)
                    self.database.commit()
                    results = cursor.rowcount
                    if results:
                        self.add_operation(goods.goods_id, 0)
                        return goods
                    else:
                        return False
                else:
                    return False
            except Exception as error:
                self.database.rollback()
                show(str(error))
                return "had_error"
            finally:
                self.database.close()

    def add_operation(self, goods_id, operation_code):
        """
        :param
        goods_id:
        operation_code:
        0:ADD
        1:SEND_MESSAGE
        2:PICK_UP
        """
        operation = ""
        if 0 == operation_code:
            operation = "ADD"
        elif 1 == operation_code:
            operation = "SEND_MESSAGE"
        elif 2 == operation_code:
            operation = "PICK_UP"
        self.connectDB()
        if self.database is None:
            return "had_error"
        else:
            cursor = self.database.cursor()
            sql = "INSERT INTO Operation_record(goods_id, operation) values(%s, %s)"
            parm = (goods_id, operation)
            try:
                cursor.execute(sql, parm)
                self.database.commit()
            except Exception as error:
                self.database.rollback()
                show(str(error))
                return "had_error"

    def confirm_code(self, goods_id, pick_up_code):
        self.connectDB()
        if self.database is None:
            return "had_error"
        else:
            cursor = self.database.cursor()
            confirm_sql = "SELECT count(1) FROM Goods_Information WHERE goods_id = %s AND pick_up_code = %s"
            parm = (goods_id, pick_up_code)
            flag = None
            try:
                cursor.execute(confirm_sql, parm)
                self.database.commit()
                results = cursor.fetchone()
                # 确认快递提货码是否正确
                if results[0]:
                    flag = True
                else:
                    flag = False
            except Exception as error:
                self.database.rollback()
                show(str(error))
                return "had_error"
            finally:
                self.database.close()
            return flag

