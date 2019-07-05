function send() {
    parent.xadmin.add_tab('短信发送', '/show_send_goods_list', true);
}

function pickUp(obj) {
    var goodsid = $(obj).parents('tr').children('input').val();
    var data = {"goodsId": goodsid};

    layer.confirm('您确定进行手动收货吗？', {
        btn: ['确定', '取消'] //按钮
    }, function () { //确认
        //ajax请求登入接口
        $.ajax({
            type: 'POST',
            async: true,
            //异步请求（同步请求将会锁住浏览器，用户其他操作必须等待请求完成才可以执行）
            url: '/pickUp',
            data: JSON.stringify(data),
            contentType: "application/json;charset=UTF-8",
            success: function (result) {
                if (result == "success") {
                    layer.msg('收货完成', {icon: 1});
                } else if (result == "fail") {
                    layer.msg('收货失败，请重试或联系管理员！', {icon: 2});
                }
                setTimeout(function () {
                    location.reload();
                }, 1000);
            },
            error: function (result) {
                layer.alert("服务器异常——" + result);
                location.reload();
            }
        })
    });
}