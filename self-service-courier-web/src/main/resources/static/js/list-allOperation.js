layui.use(['laydate', 'form'],
    function () {
        var laydate = layui.laydate;
        //执行一个laydate实例
        laydate.render({
            elem: '#operationTime' //指定元素
        });
    });

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
                    url: '/OperationSearch',
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
                            html += "<tr><td>" + item.expressNumber + "</td>" + "<td>" + item.operation + "</td>" + "<td>" + timeFormat(item.operationTime) + "</td>"
                        }
                        $("#tbody").html(html);
                    },
                    error: function (result) {
                    }
                });
            });
    });


function timeFormat(time) {
    var d = new Date(time);

    var year = d.getFullYear();       //年
    var month = d.getMonth() + 1;     //月
    var day = d.getDate();            //日

    var hh = d.getHours();            //时
    var mm = d.getMinutes();          //分
    var ss = d.getSeconds();           //秒

    var clock = year + "-";

    if (month < 10)
        clock += "0";

    clock += month + "-";

    if (day < 10)
        clock += "0";

    clock += day + " ";

    if (hh < 10)
        clock += "0";

    clock += hh + ":";
    if (mm < 10) clock += '0';
    clock += mm + ":";

    if (ss < 10) clock += '0';
    clock += ss;
    return (clock);
}
