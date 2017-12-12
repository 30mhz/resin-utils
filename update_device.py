from devices import details, update
system("clear") # Linux - OSX only :(
UUID = raw_input("Enter device UUID to update: ")
system("clear") # Linux - OSX only :(
print details(UUID)
readkey()
COMMIT = raw_input("Enter commit to set:")
readkey()
