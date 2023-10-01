import frida
import sys

rdev = frida.get_remote_device()
# process = rdev.enumerate_processes()#获取手机所有进程
session = rdev.attach("车智赢+")

with open("./che.js", "r", encoding="utf-8") as f:
    hk_js = f.read()

print(hk_js)

def on_message(message, data):
    if message["type"] == "send":
        print(message['payloay'])
script = session.create_script(hk_js)
script.on("message", on_message)
script.load()

sys.stdin.read()