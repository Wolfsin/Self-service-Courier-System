package com.wolf.selfservicecourierweb.Entity;

import com.baomidou.mybatisplus.annotation.IdType;
import com.baomidou.mybatisplus.annotation.TableField;
import com.baomidou.mybatisplus.annotation.TableId;
import com.baomidou.mybatisplus.annotation.TableName;
import lombok.Data;

@Data
@TableName("Goods_Information")
public class Goods {
    @TableId(type = IdType.AUTO)
    private Integer goodsId;
    private String expressNumber;
    private String phone;
    private String containerNumber;
    private String pickUpCode;
    @TableField(exist = false)
    private String status;
    @TableField(exist = false)
    private String lastOperationTime;
}
