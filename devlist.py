import general

system("clear") # Linux - OSX only :(
from devices import devlist
for items in devlist():
    print ("%s\t%s" % (items[1],items[0]))
# print ("Devices:")
# readkey()
# system("clear") # Linux - OSX only :(
raw_input ("Press enter to continue")
