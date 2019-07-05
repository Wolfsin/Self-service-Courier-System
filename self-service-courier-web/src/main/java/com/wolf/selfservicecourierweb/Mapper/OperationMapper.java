package com.wolf.selfservicecourierweb.Mapper;

import com.baomidou.mybatisplus.core.mapper.BaseMapper;
import com.wolf.selfservicecourierweb.Entity.Operation;
import org.apache.ibatis.annotations.Param;
import org.apache.ibatis.annotations.Select;

import java.sql.Timestamp;
import java.util.List;

public interface OperationMapper extends BaseMapper<Operation> {
    @Select("SELECT Goods_Information.goods_id," +
            " express_number," +
            " (case operation when 'ADD' then '入库' when 'SEND_MESSAGE' then '发送短信' when 'PICK_UP' then '确认收货' end)operation," +
            " operation_time" +
            " FROM Goods_Information" +
            " LEFT JOIN Operation_record ON Goods_Information.goods_id= Operation_record.goods_id" +
            " ORDER BY Goods_Information .goods_id,operation_time")
    List<Operation> selectAll();

    @Select("<script>" +
            "SELECT Goods_Information.goods_id," +
            " express_number," +
            " (case operation when 'ADD' then '入库' when 'SEND_MESSAGE' then '发送短信' when 'PICK_UP' then '确认收货' end)operation," +
            " operation_time" +
            " FROM Goods_Information" +
            " LEFT JOIN Operation_record ON Goods_Information.goods_id= Operation_record.goods_id" +
            " <if test='goods_id!=null or operation!=null or operation_time!=null'>" +
            " WHERE" +
            " </if>" +
            " <if test='goods_id!=null'>" +
            " Goods_Information.goods_id = #{goods_id} " +
            " </if>" +
            " <if test='goods_id!=null and (operation!=null or operation_time!=null) '>" +
            " AND" +
            " </if>" +
            " <if test='operation!=null'>" +
            " operation = #{operation}" +
            " </if>" +
            " <if test='operation!=null and operation_time!=null '>" +
            " AND" +
            " </if>" +
            " <if test='operation_time!=null'>" +
            " to_days(operation_time) = to_days(#{operation_time})" +
            " </if>" +
            " ORDER BY Goods_Information .goods_id,operation_time" +
            "</script>")
    List<Operation> selectBySearch(@Param("goods_id") Integer goods_id, @Param("operation") String operation, @Param("operation_time") Timestamp operation_time);
}
