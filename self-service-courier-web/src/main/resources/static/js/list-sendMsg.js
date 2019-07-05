function send(obj) {
    var goodsid = $(obj).parents('tr').children('input').val();
    var goodsExpressNumber = $($(obj).parents('tr').children('td')[0]).text();
    var phone = $($(obj).parents('tr').children('td')[1]).text();
    var index = layer.open({
        type: 2,
        area: [460 + 'px', 180 + 'px'],
        fix: false, //不固定
        maxmin: true,
        shadeClose: true,
        shade: 0.4,
        title: "快递单号：" + goodsExpressNumber,
        content: "/showSendMsg?goodsid=" + goodsid + "&phone=" + phone,
        end: function () {
            location.reload();
        }
    });

}