Java.perform(function (){
    var addr_func = Module.findExportByname("LibJNIEncrypt.so","AES_128_ECB_FKCS5Padding_Encrypt");

    Interceptor.attach(addr_func, {
        onEnter: function (args){

        },

        onLeave: function (retValue){

        }

    })


})