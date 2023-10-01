Java.perform(function() {

    // 找包、类
    var UserModel = Java.use("com.che168.autotradercloud.user.model.UserModel");

    // Hook，替换 implementation固定语法
    UserModel.loginByPassword.implementation = function(str, str1, str2, callback){
        // 输出参数看一下
        console.log(str);
        console.log(str1);
        console.log(str2);

        // 输出字典 如果有字典参数可使用Java.use("")导入java的包，进行可视化字典
        var Map = Java.use('java.util.HashMap');
        var obj = Java.cast(map, Map);
        console.log('字典的值为->',obj.tostring())

        // 查看所有调用栈
        console.log(Java.use("android.util.Log").getStackTraceString(Java.use("java.lang.Throwable").$new()))

        //执行源来的方法 如果有返回值用return 返回
        var res = this.loginByPassword(str, str1, str2, callback);
        return res;
    }


})