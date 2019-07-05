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

import javax.servlet.http.HttpSession;
import java.util.Map;

@Controller
public class LoginController {
    @Autowired
    private UserMapper userMapper;

    @RequestMapping(value = {"/", "/login", "/login.html"})
    public String Login() {
        return "login";
    }

    @RequestMapping("/index")
    public String LoginSuccess(Map<String, Object> map, HttpSession session) {
        Object username = session.getAttribute("username");
        if (username == null) {
            return "login";
        } else {
            map.put("username", username.toString());
            return "index";
        }
    }

    @RequestMapping("/logout")
    public String Logout(HttpSession session) {
        session.invalidate();
        return "login";
    }

    @PostMapping("/loginPost")
    @ResponseBody
    public String loginPost(@RequestBody User user, HttpSession session) {
        try {
            int count = userMapper.selectCount(new QueryWrapper<User>().eq("username", user.getUsername()).eq("password", user.getPassword()));
            if (count == 0) {
                return "passwordError";
            }
            session.setAttribute("username", user.getUsername());
            return "success";
        } catch (Exception error) {
            return error.toString();
        }
    }
}
