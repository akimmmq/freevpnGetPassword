import requests

from pyperclip import copy
from bs4 import BeautifulSoup

#
#  Comment section
# 

#  There may be only 2 types of errors:
        # 1) You don't have internet connection
        # 2) Site freevpn.me/accounts/ don't exist :C
#
def GetPassword():
    try:
        link = 'https://freevpn.me/accounts/' 
        responce = requests.get(link).text # We are getting html code from freevpn.me
        dataSite = BeautifulSoup(responce , 'lxml')
        findServer1 = dataSite.find('div' , id = 'server-1-tab-0') # We are choosing server, that need for us
        findBlock = findServer1.find_all('li')[2].text  # Get password line (password: herepasswordfromsite)
        password = findBlock.split()[1] # Get password value
        copy(password) # Copy it to clipboard using pyperclip
        return True
    except:
        # If we get some problems just return False 
        return False