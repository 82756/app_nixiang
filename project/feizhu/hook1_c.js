var  targetClass = "com.alibaba.wireless.security.middletierplugin.c.a.a$a";
Java.enumerateClassLoaders({
    onMatch: function (loader) {
        try {
            var iUseCls = loader.findClass(targetClass);
            if(iUseCls){
                console.log("loader find: " + loader);
            }

        } catch (error) {
            //console.log("classloader failed" + error);
        }
    }, onComplete: function () {

    }
});

// frida -Uf com.taobao.trip -l hook.js
// frida -Uf com.taobao.trip -l hook.js -o all_interceptor3.txt

