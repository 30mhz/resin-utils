import general
system("clear") # Linux - OSX only :(
print ("Select Application to check settings:")
print #newline
print ("ID\tNAME")
import application
applications, shortlist = application.list()
for items in shortlist:
    print ("%s\t%s" % (items[1], items[0]))
print #newline
ID = input("Please enter application ID: ")
try:
    system("clear") # Linux - OSX only :(
    application.check(ID)
except:
    print "Retrieve error."
    print "Press a key to continue."
readkey()
