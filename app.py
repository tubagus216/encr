
from help.util import futil
from help import encr

def init(arg):
    if arg[0] == "run":
        if len(arg) >= 3:
            if arg[2] == "--exec":
               arch = futil.listAndEcrypt(arg[1]) 
               
                   
    elif arg[0] == "decrypt":
        print(arg[1])

