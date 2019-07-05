function change() {
    $("#phone").removeAttr("disabled");
    $("#phone").removeClass("layui-disabled");
}

layui.use('form',
    function () {
        var form = layui.form;
        //监听提交
        form.on('submit(send)',
            function (data) {
                //ajax请求登入接口
                $.ajax({
                    type: 'POST',
                    async: true,
                    //异步请求（同步请求将会锁住浏览器，用户其他操作必须等待请求完成才可以执行）
                    url: '/sendMsg',
                    data: JSON.stringify(data.field),
                    contentType: "application/json;charset=UTF-8",
                    success: function (result) {
                        if (result == "success") {
                            layer.msg('发送成功！');
                        } else if (result == "fail") {
                            layer.msg('发送失败，请联系系统管理员！');
                        }
                        setTimeout(function () {
                            parent.layer.closeAll()
                        }, 1000);
                    },
                    error: function (result) {
                        layer.alert("服务器异常——" + result);
                    }
                });
            });
    });