package com.wolf.selfservicecourierweb.Entity;

import com.baomidou.mybatisplus.annotation.IdType;
import com.baomidou.mybatisplus.annotation.TableId;
import com.baomidou.mybatisplus.annotation.TableName;
import lombok.Data;

@Data
@TableName("User")
public class User {
    @TableId(type = IdType.AUTO)
    private Integer userid;
    private String username;
    private String password;
    private String phonenumber;
}
