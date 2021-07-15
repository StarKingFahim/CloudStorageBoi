import os
import dropbox

class TransferData:
    def __init__(self,access_token):
        self.access_token = access_token

    def uploadFiles(file_from):
      dbx = dropbox.Dropbox(self.access_token)
      for root,dirs,files in os.walk(file_from):
          relative_path = os.path.relpath(local_path,file_from)
          dropbox_path = os.path.join(file_to,relative_path)
          with open(local_path,'rb') as f:
              dbx.files.upload(f.read(),dropbox.path,mode=WriteMode('overwrite'))
    
def main():
    access_token = "sl.A0pTIpfcENpR5IJCzZId-zms5dHj-ifIig2eKFBpsW4byT5TBZ-gTGXjl9DCDGikniBLv4vTpdbI7y1XWMHzGvGWGArGnGg899QdwNetbJ5SMcxG8vFSdqvQJ6dPbBlcVkGbdGA"
    transferData = TransferData(access_token)

    file_from = input("Enter the file path to transfer: ")
    file_to = input("Enter the full path to transfer to dropbox: ")

    transferData.upload_file(file_from, file_to)
    print("Transfer Successful")