#python script to generate streamable google drive video link |
#-------------------------------------------------------------

#importing pyperclip module
import pyperclip

#importing os module
import os

#importing google drive apikey
apikey = "AIzaSyArzREFjCHdvOuE4TWqp79L7dAjV6DC3jE"

#importing drive link 
drivelink= input("Enter drive link ==>")

#cutting drive id from drive link using index numbers
driveid=drivelink[32:-17]

#generating streamable drive link 
streamable="https://www.googleapis.com/drive/v3/files/"+driveid+"?alt=media&key="+apikey

#coping generated drive link to clipboard using pyperclip module
pyperclip.copy(streamable)

#starting vlc player by os module
os.system("start vlc")

#Then go to your vlc player's open network stream tab by using 'CTRL+N' keyboard shortcut key,press 'CTRL+A' and then press 'CTRL+V'.