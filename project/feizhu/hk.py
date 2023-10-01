import frida
import sys

"""
at mtopsdk.mtop.protocol.builder.impl.InnerProtocolParamBuilderImpl.buildParams(Native Method)
	at mtopsdk.framework.filter.before.ProtocolParamBuilderBeforeFilter.b(ProtocolParamBuilderBeforeFilter.java:45)
	at mtopsdk.framework.manager.impl.AbstractFilterManager.a(AbstractFilterManager.java:60)
	at mtopsdk.mtop.intf.MtopBuilder$1.run(MtopBuilder.java:879)
	at java.util.concurrent.Executors$RunnableAdapter.call(Executors.java:462)
	at java.util.concurrent.FutureTask.run(FutureTask.java:266)
	at java.util.concurrent.ThreadPoolExecutor.runWorker(ThreadPoolExecutor.java:1167)
	at java.util.concurrent.ThreadPoolExecutor$Worker.run(ThreadPoolExecutor.java:641)
	at java.lang.Thread.run(Thread.java:919)
	at mtopsdk.mtop.util.MtopSDKThreadPoolExecutorFactory$MtopSDKThreadFactory$1.run(MtopSDKThreadPoolExecutorFactory.java:68)

 ========== 
name:c	value:com.alibaba.wireless.security.open.SecurityGuardManager@e0f5ccc
name:d	value:com.alibaba.wireless.security.middletierplugin.c.a.a$a@c98db15
name:e	value:null
name:f	value:null
 ========== 

"""

rdev = frida.get_remote_device()
# process = rdev.enumerate_processes()#获取手机所有进程
session = rdev.attach("飞猪旅行")

with open("./hook.js", "r", encoding="utf-8") as f:
    hk_js = f.read()

print(hk_js)

def on_message(message, data):
    print(message)
    if message['type'] == 'error':
        print(message['description'])
        print(message['stack'])
    if message["type"] == "send":
        print(message['payloay'])
script = session.create_script(hk_js)
script.on("message", on_message)
script.load()

sys.stdin.read()