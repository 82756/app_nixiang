import codecs
import frida
import time


hook_code = '''
rpc.exports = {
    // 函数名encrypt
    encrypt: function(localtime,data){
        var sig;
        Java.perform(function(){
            var map1 = Java.use('java.util.HashMap').$new();
            var map2 = Java.use('java.util.HashMap').$new();
            var str1 = "12663307";
            var str2 = null;
            var b1 = false;
            var str3 = "r_117";
            
            map1.put("data",data);
            map1.put("deviceId","ArLGY7s64LdnHc70_ueTkoXl2-ZUDNz0ltdgD0s5txQq");
            map1.put("sid","182b219b523ce715a3b61f8fdbf09754");
            map1.put("uid","2207560347204");
            map1.put("x-features","27");
            map1.put("appKey","12663307")
            map1.put("api","mtop.trip.search.dinamicx.pattern.render");
            map1.put("utdid","ZQPNHxmNzyADACL2ehl/Y/Xw");
            map1.put("extdata","openappkey=DEFAULT_AUTH");
            map1.put("ttid","10002659@travel_android_9.9.32.104");
            map1.put("t",localtime);
            map1.put("v","1.0");
            
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
            
            // console.log(map1);
            console.log(map1.get("data"));
            
            

            // use 加载的类路径
            var InnerSignImpl = Java.use('mtopsdk.security.InnerSignImpl').$new()
            InnerSignImpl.b(Java.use("mtopsdk.mtop.global.MtopConfig").$new("INNER"));
            sig = InnerSignImpl.a(map1,map2,str1,str2,b1,str3);
        }
    )
    return sig.toString();
    
    }
};
'''

def on_message(message, data):
    if message['type'] == 'send':
        print(message['payload'])
    elif message['type'] == 'error':
        print(message['stack'])

process = frida.get_usb_device().attach('飞猪旅行')
script = process.create_script(hook_code)
script.on('message', on_message)
script.load()

def d_rpc(localtime,data):
    dy = script.exports.encrypt(f"{localtime}",data)
    return dy

# print(d_rpc("1"))
