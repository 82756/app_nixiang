Java.perform(function(){
    // umid的地方
    var FishUmidHelper = Java.use("com.taobao.idlefish.xframework.util.FishUmidHelper")
    FishUmidHelper.a.implementation = function (params){
        // 查看所有调用栈
        console.log(Java.use("android.util.Log").getStackTraceString(Java.use("java.lang.Throwable").$new()))
        console.log(params);
        var res = this.a(params)
        console.log(res);
        return res;
    }

    var StringUtils = Java.use("com.alibaba.analytics.utils.StringUtils")
    StringUtils.a.overload('java.util.Map').implementation = function (obj) {
        console.log("obj------------->",obj)
        var res = this.a(obj);
        console.log(res);
        return res;
    }

    var InnerSignImpl = Java.use("mtopsdk.security.InnerSignImpl")
    InnerSignImpl.getMiniWua.implementation = function(mp,str1){
        console.log("/////////////////////////////////")
        console.log(mp)
        console.log(str1)

        var res = this.getMiniWua(mp,str1)
        console.log(res)
        console.log("/////////////////////////////////")
        return res;
    }

    var LocalInnerSignImpl = Java.use("mtopsdk.security.LocalInnerSignImpl")
    LocalInnerSignImpl.getMtopApiSign.implementation = function(mp,str1,str2){
        console.log("/////////////////////////////////")
        console.log(mp)
        console.log(str1)
        console.log(str2)
        var res = this.getMtopApiSign(mp,str1,str2)
        console.log(res)
        console.log("/////////////////////////////////")
        return res;
    }

    // var InnerNetworkConverter = Java.use("mtopsdk.mtop.protocol.converter.impl.InnerNetworkConverter")
    // InnerNetworkConverter.a.implementation = function () {
    //     var res = this.a()
    //     console.log(res)
    //     var keyset = res.keySet();
    //     var it = keyset.iterator();
    //     while(it.hasNext()){
    //         var keystr = it.next().toString();
    //         var valuestr = res.get(keystr).toString();
    //         console.log(keystr)
    //         console.log(valuestr)
    //     }
    //     return res
    //
    // }

    // var ClientInfo = Java.use("com.taobao.android.remoteobject.core.ClientInfo")
    // ClientInfo.setClientHeader.implementation = function (res){
    //
    //     console.log("getClientHeader----------->",res)
    //     var keyset = res.keySet();
    //     var it = keyset.iterator();
    //     while(it.hasNext()){
    //         var keystr = it.next().toString();
    //         var valuestr = res.get(keystr).toString();
    //         console.log(keystr)
    //         console.log(valuestr)
    //     }
    //     return this.setClientHeader(res)
    // }

    // url的名字
    var BaseApiProtocol = Java.use("com.taobao.idlefish.protocol.net.api.BaseApiProtocol")
    BaseApiProtocol.getApiName.implementation = function(){
        var res = this.getApiName()
        console.log(res);
        return res;
    }

    // 发包地方，暂时无法抓取到
    var MtopSend = Java.use("com.taobao.android.remoteobject.easy.MtopSend")
    MtopSend.send.implementation = function (obj1, obj2){
        console.log(obj1,obj2);
        var res = this.send(obj1, obj2);
        console.log(res);
        return res;

    }



})

//frida -Uf com.taobao.idlefish -l hook.js