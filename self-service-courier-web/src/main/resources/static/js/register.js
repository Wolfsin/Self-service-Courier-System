$(function () {
    layui.define('form', function (exports) {
        var form = layui.form;
        //自定义验证
        form.verify({
            username: function (value, item) { //value：表单的值、item：表单的DOM对象
                if (!new RegExp("^[a-zA-Z0-9_\u4e00-\u9fa5\\s·]+$").test(value)) {
                    return '用户名不能有特殊字符';
                }
                if (/(^\_)|(\__)|(\_+$)/.test(value)) {
                    return '用户名首尾不能出现下划线\'_\'';
                }
                if (/^\d+\d+\d$/.test(value)) {
                    return '用户名不能全为数字';
                }
            }
            //我们既支持上述函数式的方式，也支持下述数组的形式
            //数组的两个值分别代表：[正则匹配、匹配不符时的提示文字]
            , password: [
                /^[\S]{6,12}$/
                , '密码必须6到12位，且不能出现空格'
            ]
            , repassword: function (value, item) {
                if ($("input[name='repassword']").val() != $("input[name='password']").val()) {
                    return '两次密码不一致！';
                }
            }
            , phone: [
                /^[1]([3-9])[0-9]{9}$/
                , '请输入正确的中国手机号码'
            ]
            , registercode: function (value, item) {
                if (value != "123456") {
                    return '请输入正确的许可码，如果没有许可码请联系管理员！'
                }
            }
        });
    });
    layui.use('form',
        function () {
            var form = layui.form;
            //监听提交
            form.on('submit(register)',
                function (data) {
                    //ajax请求登入接口
                    $.ajax({
                        type: 'POST',
                        async: true,
                        //异步请求（同步请求将会锁住浏览器，用户其他操作必须等待请求完成才可以执行）
                        url: '/registerPost',
                        data: JSON.stringify(data.field),
                        contentType: "application/json;charset=UTF-8",
                        success: function (result) {
                            if (result == 'success') {
                                layer.msg("注册成功" + data.field.username + '，欢迎使用', {
                                        offset: '15px',
                                        icon: 1,
                                        time: 1500
                                    },
                                    function () {
                                        location.href = '../'; //
                                    });
                            } else if (result == 'usernameRepeat') {
                                layer.msg('用户名已存在！', {
                                        offset: '15px',
                                        icon: 2,
                                        time: 1000
                                    },
                                    function () {
                                        $("input[name='username']").val("");
                                        $("input[name='password']").val("");
                                        $("input[name='repassword']").val("");
                                        $("input[name='phonenumber']").val("");
                                    });
                            } else if (result == 'fail') {
                                layer.msg('注册失败，请稍后再试', {
                                    offset: '15px',
                                    icon: 2,
                                    time: 1000
                                }, function () {
                                    $("input[name='username']").val("");
                                    $("input[name='password']").val("");
                                    $("input[name='repassword']").val("");
                                    $("input[name='phonenumber']").val("");
                                });
                            }
                        },
                        error: function (result) {
                            alert("服务器异常---->" + result);
                        }
                    });
                });
        });
});