package com.wolf.selfservicecourierweb.Controller;

import com.baomidou.mybatisplus.core.conditions.query.QueryWrapper;
import com.baomidou.mybatisplus.core.conditions.update.UpdateWrapper;
import com.wolf.selfservicecourierweb.Entity.Goods;
import com.wolf.selfservicecourierweb.Entity.Operation;
import com.wolf.selfservicecourierweb.Entity.Status;
import com.wolf.selfservicecourierweb.Mapper.GoodsMapper;
import com.wolf.selfservicecourierweb.Mapper.OperationMapper;
import com.wolf.selfservicecourierweb.Mapper.StatusMapper;
import com.wolf.selfservicecourierweb.Tools.OperationMessage;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.transaction.annotation.Transactional;
import org.springframework.transaction.interceptor.TransactionAspectSupport;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.ResponseBody;

import java.util.HashMap;
import java.util.List;
import java.util.Map;

@Controller
public class GoodsController {
    @Autowired
    private GoodsMapper goodsMapper;
    @Autowired
    private StatusMapper statusMapper;
    @Autowired
    private OperationMapper operationMapper;

    @RequestMapping("/show_goods_list")
    public String showGoodsList(Map<String, Object> map) {
        List<Goods> goodsList = goodsMapper.selectAll();
        map.put("goodsList", goodsList);
        return "list-allGoods";
    }

    @RequestMapping("/GoodsSearch")
    @ResponseBody
    public List<Goods> GoodsSearch(@RequestBody Map<String, String> searchParam) {
        Map<String, Object> param = new HashMap<>();
        Boolean isSendMsg = null;
        Boolean isPickUp = null;
        String expressNumber = searchParam.get("expressNumber");
        String Status = searchParam.get("status");

        if ("0".equals(Status)) {
            isSendMsg = false;
            isPickUp = false;
        } else if ("1".equals(Status)) {
            isSendMsg = true;
            isPickUp = false;
        } else if ("2".equals(Status)) {
            isSendMsg = true;
            isPickUp = true;
        }
        param.put("is_send_msg", isSendMsg);
        param.put("is_pick_up", isPickUp);
        param.put("Goods_Information.express_number", expressNumber);

        List<Goods> goodsList = goodsMapper.selectBySearch(new QueryWrapper<Goods>().allEq(param, false));

        return goodsList;
    }

    @RequestMapping("/show_send_goods_list")
    public String showSendGoodsList(Map<String, Object> map) {
        List<Goods> goodsList = goodsMapper.selectNoSend();
        map.put("goodsList", goodsList);
        return "list-sendMsg";
    }

    @RequestMapping("/show_pickUp_list")
    public String showPickUpList(Map<String, Object> map) {
        List<Goods> goodsList = goodsMapper.selectNoDone();
        map.put("goodsList", goodsList);
        System.out.println(goodsList.toString());
        return "list-pickUp";
    }

    @RequestMapping("/pickUp")
    @ResponseBody
    @Transactional
    public String pickUp(@RequestBody Goods goods) {
        Status status = new Status();
        status.setIsPickUp(true);
        Operation operation = new Operation();
        operation.setGoodsId(goods.getGoodsId());
        operation.setOperation(OperationMessage.PICK_UP);
        operation.setOperationTime(null);
        try {
            statusMapper.update(status, new UpdateWrapper<Status>().eq("goods_id", goods.getGoodsId()));
            operationMapper.insert(operation);
            return "success";
        } catch (Exception e) {
            TransactionAspectSupport.currentTransactionStatus().setRollbackOnly();
            return e.toString();
        }
    }
}
