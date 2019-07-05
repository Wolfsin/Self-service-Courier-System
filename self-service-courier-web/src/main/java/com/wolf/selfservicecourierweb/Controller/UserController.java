package com.wolf.selfservicecourierweb.Controller;

import com.baomidou.mybatisplus.core.conditions.query.QueryWrapper;
import com.baomidou.mybatisplus.core.conditions.update.UpdateWrapper;
import com.wolf.selfservicecourierweb.Entity.User;
import com.wolf.selfservicecourierweb.Mapper.UserMapper;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.ResponseBody;

import javax.servlet.http.HttpSession;
import java.util.Map;

@Controller
public class UserController {

    @Autowired
    private UserMapper userMapper;

    @RequestMapping("/member")
    public String gerUsername(Map<String, Object> map, HttpSession session) {
        Object username = session.getAttribute("username");
        map.put("username", username.toString());
        return "member";
    }

    @RequestMapping("/changePassword")
    @ResponseBody
    public String changPassword(@RequestBody Map<String, String> userinfo) {
        String username = userinfo.get("username");
        String oldPassword = userinfo.get("old-password");
        String newPassword = userinfo.get("password");
        User user = new User();
        user.setPassword(newPassword);
        int count = userMapper.selectCount(new QueryWrapper<User>().eq("username", username).eq("password", oldPassword));
        if (count == 0) {
            return "fail";
        } else {
            userMapper.update(user, new UpdateWrapper<User>().eq("username", username));
            return "success";
        }
    }
}
