Java.perform(function() {
    // 找包、类
    var InitJob = Java.use("com.fscxtxy.nohttp.NoHttpUtil");
    var i = Java.use("android.provider.Settings")
    var sc = Java.use("android.content.ContentResolver")
    var visi = Java.use("android.app.Activity")

    var Ws = Java.use("android.provider.Settings$System")

    Ws.getString.implementation = function (a,b){
        console.log(b)
        console.log(a)
        return this.getString(a,b)
    }

    // Hook，替换 implementation固定语法
    InitJob.doLogin.implementation = function(a,b,c,d,e){
        // 输出参数看一下
        console.log(a);
        console.log(b);
        console.log(c);


        c="1574d7e76627feb2"

        //执行源来的方法 如果有返回值用return 返回
        var res = this.doLogin(a,b,c,d,e);
        return res
    }


})