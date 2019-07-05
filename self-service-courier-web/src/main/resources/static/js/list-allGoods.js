layui.use('form',
    function () {
        var form = layui.form;
        //监听提交
        form.on('submit(search)',
            function (data) {
                //ajax请求登入接口
                $.ajax({
                    type: 'POST',
                    async: true,
                    //异步请求（同步请求将会锁住浏览器，用户其他操作必须等待请求完成才可以执行）
                    url: '/GoodsSearch',
                    data: JSON.stringify(data.field),
                    contentType: "application/json;charset=UTF-8",
                    dataType: "json",
                    success: function (result) {
                        var html = "";
                        $("#tbody").empty();
                        if (result.length == 0) {
                            layer.msg('未查到有效数据，请确认搜索条件!');
                            return false;
                        }
                        for (var i = 0; i < result.length; i++) {
                            var item = result[i];
                            html += "<tr><td>" + item.expressNumber + "</td>" + "<td>" + item.phone + "</td>" + "<td>" +
                                item.containerNumber + "</td>" + "<td>" + item.pickUpCode + "</td>" + "<td>" + item.status + "</td>"
                        }
                        $("#tbody").html(html);
                    },
                    error: function (result) {
                    }
                });
            });
    });
