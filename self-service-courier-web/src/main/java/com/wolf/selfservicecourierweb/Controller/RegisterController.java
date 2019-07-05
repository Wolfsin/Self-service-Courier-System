package com.wolf.selfservicecourierweb.Controller;

import com.baomidou.mybatisplus.core.conditions.query.QueryWrapper;
import com.wolf.selfservicecourierweb.Entity.User;
import com.wolf.selfservicecourierweb.Mapper.UserMapper;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.ResponseBody;

@Controller
public class RegisterController {
    @Autowired
    private UserMapper userMapper;

    @RequestMapping(value = {"/register"})
    public String Register() {
        return "register";
    }

    @PostMapping("/registerPost")
    @ResponseBody
    public String registerPost(@RequestBody User user) {
        try {
            int count = userMapper.selectCount(new QueryWrapper<User>().eq("username", user.getUsername()));
            if (count == 0) {
                int success = userMapper.insert(user);
                if (success != 0) {
                    return "success";
                } else {
                    return "fail";
                }
            } else {
                return "usernameRepeat";
            }
        } catch (Exception e) {
            return e.toString();
        }
    }
}
