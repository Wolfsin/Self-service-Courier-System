package com.wolf.selfservicecourierweb.Entity;

import com.baomidou.mybatisplus.annotation.IdType;
import com.baomidou.mybatisplus.annotation.TableId;
import com.baomidou.mybatisplus.annotation.TableName;
import lombok.Data;

@Data
@TableName("Goods_Status")
public class Status{
    @TableId(type = IdType.AUTO)
    private Integer statusId;
    private Integer goodsId;
    private String expressNumber;
    private Boolean isSendMsg;
    private Boolean isPickUp;
}
