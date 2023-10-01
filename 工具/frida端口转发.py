import subprocess

subprocess.getoutput("adb forward tcp:27042 tcp:27042")
subprocess.getoutput("adb forward tcp:27043 tcp:27043")

subprocess.getoutput("adb -s 928QAEVJ225S3 forward tcp:27042 tcp:27042")
subprocess.getoutput("adb -s 928QAEVJ225S3 forward tcp:27043 tcp:27043")

subprocess.getoutput("adb -s emulator-5554 forward tcp:27042 tcp:27042")
subprocess.getoutput("adb -s emulator-5554 forward tcp:27043 tcp:27043")

