
from zipfile import ZipFile
import os
from os.path import basename
from help import encr

def archive(path):

    zibObj = ZipFile('sample.zip', 'w')

    for folderName, subFolder, filenames in os.walk(path):
        for filename in filenames:
            filePath = os.path.join(folderName, filename)
            print("Adding files: "+filePath)
            zibObj.write(filePath.replace("./", ""), filePath)
    return True

def listAndEcrypt(path):
    if os.path.isdir(path):
        list(path)
    else:
        addToEncript(path)
    

def list(path):
    for folderName, subFolder, filenames in os.walk(path):
        for filename in filenames:
            filePath = os.path.join(folderName, filename)
            addToEncript(filePath)



def addToEncript(path):
    if os.path.isdir(path):
        list(path)
    else:
        if path.find('.encr') == -1:
            encr.encrypt(path)
            os.remove(path)
            print("Encrypting file: "+os.path.abspath(path))
    