package com.wolf.selfservicecourierweb.Mapper;

import com.baomidou.mybatisplus.core.conditions.Wrapper;
import com.baomidou.mybatisplus.core.mapper.BaseMapper;
import com.baomidou.mybatisplus.core.toolkit.Constants;
import com.wolf.selfservicecourierweb.Entity.Goods;
import org.apache.ibatis.annotations.Param;
import org.apache.ibatis.annotations.Select;

import java.util.List;

public interface GoodsMapper extends BaseMapper<Goods> {

    @Select("SELECT Goods_Information.goods_id," +
            " Goods_Information.express_number," +
            " phone," +
            " container_number," +
            " pick_up_code," +
            " (case when is_send_msg = '0' and is_pick_up = '0' then '未发送短信'" +
            "  when is_send_msg = '1' and is_pick_up = '0' then '已发送短信，未收货'" +
            "  when is_pick_up = '1' then '已确认收货' end)AS status " +
            " FROM Goods_Information" +
            " LEFT JOIN Goods_Status ON Goods_Information.goods_id= Goods_Status.goods_id" +
            " ORDER BY Goods_Information.goods_id")
    List<Goods> selectAll();

    @Select("SELECT Goods_Information.goods_id," +
            " Goods_Information.express_number," +
            " phone," +
            " container_number," +
            " pick_up_code," +
            " (case when is_send_msg = '0' and is_pick_up = '0' then '未发送短信'" +
            "  when is_send_msg = '1' and is_pick_up = '0' then '已发送短信，未收货'" +
            "  when is_send_msg = '1' and is_pick_up = '1' then '已确认收货' end)AS status " +
            " FROM Goods_Information" +
            " LEFT JOIN Goods_Status ON Goods_Information.goods_id= Goods_Status.goods_id" +
            " ${ew.customSqlSegment}" +
            " ORDER BY Goods_Information.goods_id")
    List<Goods> selectBySearch(@Param(Constants.WRAPPER) Wrapper wrapper);

    @Select("SELECT Goods_Information.goods_id," +
            " Goods_Information.express_number," +
            " phone," +
            " container_number," +
            " pick_up_code," +
            " (case when is_send_msg = '0' and is_pick_up = '0' then '未发送短信'" +
            "  when is_send_msg = '1' and is_pick_up = '0' then '已发送短信，未收货'" +
            "  when is_send_msg = '1' and is_pick_up = '1' then '已确认收货' end)AS status " +
            " FROM Goods_Information" +
            " LEFT JOIN Goods_Status ON Goods_Information.goods_id= Goods_Status.goods_id" +
            " WHERE is_send_msg = '0' AND is_pick_up = '0'"+
            " ORDER BY Goods_Information.goods_id")
    List<Goods> selectNoSend();

    @Select("SELECT Goods_Information.goods_id," +
            " Goods_Information.express_number," +
            " phone," +
            " container_number," +
            " pick_up_code," +
            " (case when is_send_msg = '0' and is_pick_up = '0' then '0'" +
            "  when is_send_msg = '1' and is_pick_up = '0' then '1' end)AS status, " +
            " MAX(operation_time)AS lastOperationTime"+
            " FROM Goods_Information" +
            " LEFT JOIN Goods_Status ON Goods_Information.goods_id= Goods_Status.goods_id" +
            " LEFT JOIN Operation_record ON Goods_Information.goods_id= Operation_record.goods_id"+
            " WHERE is_pick_up = '0'"+
            " GROUP BY Goods_Information.goods_id," +
            "          is_send_msg"+
            " ORDER BY Goods_Information.goods_id")
    List<Goods> selectNoDone();
}
