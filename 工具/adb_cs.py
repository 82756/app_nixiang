import subprocess

cmd = 'adb shell "cd data && cd local && cd tmp && ./frida-16.0.1"'

def adb_shell(cmd):
    p = subprocess.getstatusoutput(cmd)
    return p

result = adb_shell(cmd)
print(result)