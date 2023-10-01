Java.perform(function() {

    // 包、类
    var UserModel = Java.use("com.che168.autotradercloud.user.model.UserModel");
    var AppUtils = Java.use("com.che168.autotradercloud.util.AppUtils");
    var SecurityUtil = Java.use("com.autohome.ahkit.utils.SecurityUtil")

    // Hook，替换
    UserModel.loginByPassword.implementation = function(str, str1, str2, callback){
        // 输出看一下
        console.log(str);
        console.log(str1);
        console.log(str2);

        //执行源来的方法
        this.loginByPassword(str, str1, str2, callback);
    }

    AppUtils.getUDID.implementation = function (text){
        console.log(text);

        var res = this.getUDID(text);
        console.log(res);
        return res;

    }

    SecurityUtil.encode3Des.implementation = function (str1,str2){
        console.log(str1);
        console.log(str2);

        var res = this.encode3Des(str1, str2);
        console.log(res);
        return res;
    }

})