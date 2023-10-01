Java.perform(function() {

    // 找包、类
    var InitJob = Java.use("com.MobileTicket.InitJob");

    // Hook，替换 implementation固定语法
    InitJob.initCb.implementation = function(){
        // 输出参数看一下
        console.log();
        console.log("1")



        // 查看所有调用栈
        console.log(Java.use("android.util.Log").getStackTraceString(Java.use("java.lang.Throwable").$new()))

        //执行源来的方法 如果有返回值用return 返回
        var res = this.initCb(str);
    }


})