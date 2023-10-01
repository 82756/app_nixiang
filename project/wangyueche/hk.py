import frida
import sys

rdev = frida.get_remote_device()
# process = rdev.enumerate_processes()#获取手机所有进程
session = rdev.attach("朔州95128")

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