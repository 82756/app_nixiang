Java.perform(function (){
    var Base64 = Java.use("android.util.Base64");

    Base64.encodeToString.overload('[B','int').implementation = function (bArr,val) {
        var res = this.encodeToString(bArr,val);
        console.log('加密了-->',res);
        return res;
    }

    Base64.decode.overload('[B','int').implementation = function (bArr,val) {
        var res = this.decode(bArr,val);
        // 查看所有调用栈
        console.log(Java.use("android.util.Log").getStackTraceString(Java.use("java.lang.Throwable").$new()))
        console.log('解密了-->',res);
        return res;
    }

})