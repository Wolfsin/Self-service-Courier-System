layui.use('form',
    function () {
        var form = layui.form;
        //监听提交
        form.on('submit(update)',
            function (data) {
                //ajax请求登入接口
                $.ajax({
                    type: 'POST',
                    async: true,
                    //异步请求（同步请求将会锁住浏览器，用户其他操作必须等待请求完成才可以执行）
                    url: '/changePassword',
                    data: JSON.stringify(data.field),
                    contentType: "application/json;charset=UTF-8",
                    success: function (result) {
                        if (result == "success") {
                            layer.msg('修改成功，请重新登陆！');
                        } else if (result == "fail") {
                            layer.msg('修改失败，请确认旧密码是否正确！');
                        }
                        setTimeout(function () {
                        }, 1000);
                    },
                    error: function (result) {
                        layer.alert("服务器异常——" + result);
                    }
                });
            });
    });