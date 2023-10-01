function hashmap888() {
    Java.perform(function () {
        Java.choose("java.util.HashMap", {
            onMatch: function (instance) {
                if (instance.toString().indexOf("Sim")) {
                    console.log("found instance", instance);
                    console.log("HashmapString", instance.toString());
                }
            }, onComplete: function () {
                console.log("search Completed!")
            }
        })
    })
}

