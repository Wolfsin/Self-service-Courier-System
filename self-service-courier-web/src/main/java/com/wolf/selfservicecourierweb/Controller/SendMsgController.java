package com.wolf.selfservicecourierweb.Controller;

import com.baomidou.mybatisplus.core.conditions.update.UpdateWrapper;
import com.wolf.selfservicecourierweb.Entity.Goods;
import com.wolf.selfservicecourierweb.Entity.Operation;
import com.wolf.selfservicecourierweb.Entity.Status;
import com.wolf.selfservicecourierweb.Mapper.GoodsMapper;
import com.wolf.selfservicecourierweb.Mapper.OperationMapper;
import com.wolf.selfservicecourierweb.Mapper.StatusMapper;
import com.wolf.selfservicecourierweb.Tools.OperationMessage;
import com.wolf.selfservicecourierweb.Tools.SendSmsTool;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.transaction.annotation.Transactional;
import org.springframework.transaction.interceptor.TransactionAspectSupport;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.ResponseBody;

import java.util.Map;

@Controller
public class SendMsgController {
    @Autowired
    private GoodsMapper goodsMapper;
    @Autowired
    private StatusMapper statusMapper;
    @Autowired
    private OperationMapper operationMapper;

    @RequestMapping("/showSendMsg")
    public String showSendFrom(String goodsid, String phone, Map<String, Object> map) {
        map.put("goodsid", goodsid);
        map.put("phone", phone);
        return "sendMsg";
    }

    @RequestMapping("/sendMsg")
    @ResponseBody
    @Transactional
    public String sendMsg(@RequestBody Goods goods) {
        Goods originalgoods = goodsMapper.selectById(goods.getGoodsId());
        Status status = new Status();
        status.setIsSendMsg(true);
        Operation operation = new Operation();
        operation.setGoodsId(goods.getGoodsId());
        operation.setOperation(OperationMessage.SEND);
        operation.setOperationTime(null);

        originalgoods.setPhone(goods.getPhone());
        String result = SendSmsTool.send(originalgoods);
        if ("0".equals(result)) {
            try {
                operationMapper.insert(operation);
                statusMapper.update(status, new UpdateWrapper<Status>().eq("goods_id", goods.getGoodsId()));
                return "success";
            } catch (Exception e) {
                TransactionAspectSupport.currentTransactionStatus().setRollbackOnly();
                return e.toString();
            }
        } else return "fail";
    }
}
