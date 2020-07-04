import pathlib
import os

class ServiceSh:

     def isSignal(self):
        patFileTemp="/tmp/shunal_temp.txt"
        patFileProx = "/tmp/shunal_prox.txt"
        fileT = pathlib.Path(patFileTemp)
        fileP =pathlib.Path(patFileProx)

        if(fileT.exists() and fileP.exists()):
            os.system("rm "+patFileTemp)
            os.system("rm " + patFileProx)
            return True
        else:
            return False