Java.perform(function() {
    // 找包、类
    // var InnerProtocolParamBuilderImpl = Java.use("mtopsdk.mtop.protocol.builder.impl.InnerProtocolParamBuilderImpl");
    // InnerProtocolParamBuilderImpl.buildParams.implementation = function (content){
    //     var res = this.buildParams(content)
    //     console.log(res)
    //
    //     // 查看所有调用栈
    //     console.log(Java.use("android.util.Log").getStackTraceString(Java.use("java.lang.Throwable").$new()))
    //     var keyset = res.keySet();
    //     var it = keyset.iterator();
    //     while(it.hasNext()){
    //         try{
    //             var keystr = it.next().toString();
    //             var valuestr = res.get(keystr).toString();
    //             console.log(keystr)
    //             console.log(valuestr)
    //         }catch (e) {
    //             console.log(e)
    //             console.log("----")
    //         }
    //
    //     }
    //     return res;
    // }

    // 加密参数
    var InnerSignImpl = Java.use("mtopsdk.security.InnerSignImpl")
    InnerSignImpl.a.overload('java.util.HashMap', 'java.util.HashMap', 'java.lang.String', 'java.lang.String', 'boolean', 'java.lang.String').implementation = function (map1,map2,str1,str2,b1,str3){
        console.log("map1------------")
        var keyset = map1.keySet();
        var it = keyset.iterator();
        while(it.hasNext()) {
            try {
                var keystr = it.next().toString();
                console.log(keystr)
                var valuestr = map1.get(keystr).toString();
                console.log(typeof map1.get(keystr))
                console.log(valuestr)
            } catch (e) {
                console.log(e)
                console.log("----")
            }
        }


        console.log("map1------------")
        var keyset1 = map2.keySet();
        var it1 = keyset1.iterator();
        while(it.hasNext()) {
            try {
                var keystr1 = it1.next().toString();
                var valuestr1 = map2.get(keystr1).toString();
                console.log(keystr1)
                console.log(valuestr1)
            } catch (e) {
                console.log(e)
                console.log("----")
            }
        }
        console.log(str1)
        console.log(str2)
        console.log(b1)
        console.log(str3)

        console.log(" ========== ");

        var fields = Java.cast(this.getClass(),Java.use('java.lang.Class')).getDeclaredFields();
        //console.log(fields);
        for (var i = 0; i < fields.length; i++) {
            var field = fields[i];
            field.setAccessible(true);
            var name = field.getName();
            var value =field.get(this)
            console.log("name:"+name+"\tvalue:"+value);
        }

        console.log(" ========== ");

        var res = this.a(map1,map2,str1,str2,b1,str3)
        console.log(res);
        return res
    }

    var m1 = Java.use("mtopsdk.mtop.global.MtopConfig")
    m1.$init.implementation = function (str) {
        console.log("MtopConfig-->",str);
        return this.$init(str);

    }


})