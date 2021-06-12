import dropbox
import os
import shutil

class TransferData:
    def __init__(self,access_token):
        self.access_token = access_token
    
    def upload_file(self,file_from,file_to):
        dbx = dropbox.Dropbox(self.access_token)

        f = open(file_from, 'rb')
        dbx.files_upload(f.read(),file_to)

        

def main():
    access_token = 'W3y17gnZxDAAAAAAAAAAAX8H7Jema0BhmERFYn1K4Qa0CdlZ2hggHA2go4JHHpC6'
    transferData = TransferData(access_token)
    file_from = input("Enter the path of the file you want to upload..")
    file_to = '/' + input("Enter the name you want to gie your file..")
    transferData.upload_file(file_from,file_to)
    print("the file has been moved..")

main()