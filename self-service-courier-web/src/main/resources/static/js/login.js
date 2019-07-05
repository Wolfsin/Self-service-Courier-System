$(function () {
    layui.use('form',
        function () {
            var form = layui.form;
            //监听提交
            form.on('submit(login)',
                function (data) {
                    //ajax请求登入接口
                    $.ajax({
                        type: 'POST',
                        async: true,
                        //异步请求（同步请求将会锁住浏览器，用户其他操作必须等待请求完成才可以执行）
                        url: '/loginPost',
                        data: JSON.stringify(data.field),
                        contentType: "application/json;charset=UTF-8",
                        success: function (result) {
                            if (result == 'success') {
                                layer.msg(data.field.username + '，欢迎回来', {
                                        offset: '15px',
                                        icon: 1,
                                        time: 1500
                                    },
                                    function () {
                                        location.href = '../index'; //
                                    });
                            } else if (result == 'passwordError') {
                                layer.msg('用户名或密码错误！', {
                                        offset: '15px',
                                        icon: 2,
                                        time: 1000
                                    },
                                    function () {
                                        $("input[name='password']").val("");
                                    });
                            }
                        },
                        error: function (result) {
                            alert("服务器异常---->" + result);
                        }
                    });
                });
            $('#register').click(function () {
                location.href = '../register'
            })
        });
});