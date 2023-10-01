//获取一个DexFile对象
var DexFile= Java.use("dalvik.system.DexFile");
var dexfile = DexFile.$new("app_path");//执行app的路径，类似Android内的DexFile dexfile = new DexFile(app_path);一样的功能
var entries = dexfile.entries();//获取所有的加载类，这个方法获取所有的加载类
var loaedClasses =[];
while(entries.hasMoreElements()){
    loadedClasses.push(entries.nextElement());//保存加载的类型
}
console.log("all dexfileLoadedClasses"+loadedClasses);