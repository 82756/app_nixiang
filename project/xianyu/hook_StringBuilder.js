Java.perform(function (){
    var StringBuilder = Java.use("java.lang.StringBuilder");

    StringBuilder.toString.implementation = function() {
        var res = this.toString();
        console.log(res);
        return res;

    }


})
