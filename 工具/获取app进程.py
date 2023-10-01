import frida

# 获取设备信息
rdev = frida.get_remote_device()
print(rdev)

# 获取所有进程
for i in rdev.enumerate_processes():
    print(i)

# 获取前台运行的app
front_app = rdev.get_frontmost_application()
print(front_app)
