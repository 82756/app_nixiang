Java.perform(function (){

    // $ 的意思是说：拿到类下的类
    var Builder = Java.use("okhttp3.OkHttpClient$Builder");

    Builder.addInterceptor.implementation = function (inner) {
        console.log(JSON.stringify(inner));
        return this.addInterceptor(inner);
    };

})

// frida -Uf com.hupu.shihuo -l hook.js
// frida -Uf com.hupu.shihuo -l hook.js -o all_interceptor3.txt

