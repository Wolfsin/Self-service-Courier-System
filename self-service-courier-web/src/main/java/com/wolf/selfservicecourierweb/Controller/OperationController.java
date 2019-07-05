package com.wolf.selfservicecourierweb.Controller;

import com.baomidou.mybatisplus.core.conditions.query.QueryWrapper;
import com.wolf.selfservicecourierweb.Entity.Goods;
import com.wolf.selfservicecourierweb.Entity.Operation;
import com.wolf.selfservicecourierweb.Mapper.GoodsMapper;
import com.wolf.selfservicecourierweb.Mapper.OperationMapper;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.ResponseBody;

import java.util.List;
import java.util.Map;

@Controller
public class OperationController {
    @Autowired
    private GoodsMapper goodsMapper;
    @Autowired
    private OperationMapper operationMapper;

    @RequestMapping("/show_operation_list")
    public String showOperationList(Map<String, Object> map) {
        List<Operation> operationsList = operationMapper.selectAll();
        map.put("operationsList", operationsList);
        return "list-allOperation";
    }

    @RequestMapping("/OperationSearch")
    @ResponseBody
    public List<Operation> OperationSearch(@RequestBody Operation operation) {
        Goods goods = new Goods();
        if ("0".equals(operation.getOperation())) {
            operation.setOperation("ADD");
        } else if ("1".equals(operation.getOperation())) {
            operation.setOperation("SEND_MESSAGE");
        } else if ("2".equals(operation.getOperation())) {
            operation.setOperation("PICK_UP");
        } else {
            operation.setOperation(null);
        }
        if (!"".equals(operation.getExpressNumber())) {
            goods = goodsMapper.selectOne(new QueryWrapper<Goods>().eq("express_number", operation.getExpressNumber()));
        } else {
            goods.setGoodsId(null);
        }
        List<Operation> operationsList = operationMapper.selectBySearch(goods.getGoodsId(), operation.getOperation(), operation.getOperationTime());
        return operationsList;

    }

}
