Java.perform(function() {

    // 找包、类
    var RequestParamsFactory = Java.use("com.commonlib.model.net.factory.RequestParamsFactory");
    // Hook，替换 implementation固定语法
    RequestParamsFactory.b.implementation = function(str1,str2){

        // 输出参数看一下
        console.log(str1);
        console.log(str2)

        // 查看所有调用栈
        console.log(Java.use("android.util.Log").getStackTraceString(Java.use("java.lang.Throwable").$new()))

        //执行源来的方法 如果有返回值用return 返回
        var res = this.b(str1,str2);
        var keyset = res.keySet();
        var it = keyset.iterator();
        while(it.hasNext()){
            var keystr = it.next().toString();
            var valuestr = res.get(keystr).toString();
            console.log(keystr)
            console.log(valuestr)
        }
        console.log(res.toString());
        return res;

    }

    var Aesutils = Java.use("com.commonlib.model.net.factory.AEsUtils")
    Aesutils.b.overload('java.lang.String','java.lang.String','java.lang.String').implementation = function (str,str2,str3){
        console.log(str)
        console.log(str2)
        console.log(str3)

        var ress = this.b(str,str2,str3)
        console.log(ress)
        return ress
    }

    var i = Java.use("com.umeng.analytics.pro.i")
    i.d.overload('java.lang.String').implementation = function(str){
        console.log(str)
        var res = this.d(str);
        console.log(res);
        return res;

    }

    var f = Java.use("com.kwad.sdk.core.webview.kwai.f")
    f.toJson.implementation = function(){
        var res = this.toJson()
        console.log(res);
        return res;
    }

})