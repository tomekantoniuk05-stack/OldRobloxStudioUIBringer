import sys
import os
from shutil import copytree
from time import sleep

DESTINATION_APP_NAME = "RobloxStudioBeta.exe" #this app has to be in the folder, where we put the file that brings the old UI

Folders = [ #folders to the Roblox Studio folder
    "Roblox",
    "Versions"
]

def get_asset(relative_path): #this function gives us the file that we can duplicate and put into Studio's setting to bring the old UI
    relative_path = os.path.join("assets", relative_path)
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)

#getting the file path
folderPath = os.environ.get("LOCALAPPDATA")
for f in Folders:
    folderPath = os.path.join(folderPath, f)

if not os.path.isdir(folderPath):
    print("Path not found")
    sleep(5)
    sys.exit(1)

files = os.listdir(folderPath)

folders = []
for f in files:
    filePath = os.path.join(folderPath, f)
    if os.path.isdir(filePath):
        folders.append(filePath)

destinationFolder = None
for f in folders:
    if os.path.isfile(os.path.join(f, DESTINATION_APP_NAME)):
        destinationFolder = f
        break

if not destinationFolder:
    print("Something went wrong")
    sleep(5)
    sys.exit(1)

#we have a valid path

#putting the file that changes the UI to the folder
if not os.path.isdir(os.path.join(destinationFolder, DESTINATION_APP_NAME)):
    clientSettings = get_asset("ClientSettings")
    copytree(clientSettings, os.path.join(destinationFolder, os.path.basename(clientSettings)), dirs_exist_ok=True)
    print("Operation successful")
    sleep(1)