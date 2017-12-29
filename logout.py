from resin import Resin
resin = Resin()

def logout():
    resin.auth.log_out()
    print("Logged out")
    exit()
