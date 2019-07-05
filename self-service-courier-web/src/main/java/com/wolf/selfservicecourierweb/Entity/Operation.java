package com.wolf.selfservicecourierweb.Entity;

import com.baomidou.mybatisplus.annotation.IdType;
import com.baomidou.mybatisplus.annotation.TableField;
import com.baomidou.mybatisplus.annotation.TableId;
import com.baomidou.mybatisplus.annotation.TableName;
import lombok.Data;
import java.sql.Timestamp;

@Data
@TableName("Operation_record")
public class Operation extends Goods{
    @TableId(type = IdType.AUTO)
    private Integer operationId;
    private Integer goodsId;
    @TableField(exist = false)
    private String expressNumber;
    private String operation;
    private Timestamp operationTime;
}
