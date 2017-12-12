import general
from devices import details
system("clear") # Linux - OSX only :(
print ("Check device UUID on dashboard or go one step back and select \"Get device list\"")
UUID = raw_input("Input your device UUID: ")
try:
    details(UUID)
    readkey()
except:
    print("UUID not corect or device not found. Press a key to continue.")
    readkey()
