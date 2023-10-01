Java.perform(function (){
    var TreeMap = Java.use("java.util.TreeMap");
    var Map = Java.use("java.util.Map");

    TreeMap.put.implementation = function (key, value) {
        if(key==='data'){
            console.log(value);
        }
        var res = this.put(key, value);
        return res;
    }


})