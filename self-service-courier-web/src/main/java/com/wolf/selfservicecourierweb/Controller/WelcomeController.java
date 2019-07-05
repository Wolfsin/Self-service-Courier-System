package com.wolf.selfservicecourierweb.Controller;

import com.baomidou.mybatisplus.core.conditions.query.QueryWrapper;
import com.wolf.selfservicecourierweb.Entity.Status;
import com.wolf.selfservicecourierweb.Mapper.GoodsMapper;
import com.wolf.selfservicecourierweb.Mapper.StatusMapper;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.RequestMapping;

import javax.servlet.http.HttpSession;
import java.util.Map;

@Controller
public class WelcomeController {

    @Autowired
    private GoodsMapper goodsMapper;
    @Autowired
    private StatusMapper statusMapper;

    @RequestMapping("/welcome")
    public String showWlecomePage(Map<String, Object> map, HttpSession session) {
        Object username = session.getAttribute("username");
        map.put("username", username.toString());
        int all_count = 0;
        int no_send_count = 0;
        int no_done_count = 0;
        try {
            all_count = goodsMapper.selectCount(null);
            no_send_count = statusMapper.selectCount(new QueryWrapper<Status>().eq("is_send_msg", "0").eq("is_pick_up", "0"));
            no_done_count = statusMapper.selectCount(new QueryWrapper<Status>().eq("is_pick_up", "0"));
        } catch (Exception e) {
            e.printStackTrace();
        } finally {
            map.put("all_number", all_count);
            map.put("no_send_number", no_send_count);
            map.put("no_done_number", no_done_count);
        }
        return "welcome";
    }

}
