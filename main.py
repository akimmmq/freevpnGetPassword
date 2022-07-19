from getPassword import GetPassword # Another file we created 

import psutil as ps

# This function need to check is openvpn proccess running
def isAppRunning(processName):
    if processName[-3::] != 'exe': # if proccess name wrote without .exe
            processName += '.exe'
            for process in ps.process_iter():
                try:
                    if processName.lower() in process.name().lower(): #Check is openvpn proccess running by cheking processes names
                        return True
                except (ps.NoSuchProcess , ps.AccessDenied , ps.ZombieProcess): # Except errors
                    pass
            return False # If we got some problems just return False

while True:
    #If openvpn running we are get password
    if isAppRunning('openvpn-gui'):
        if GetPassword(): # If all worked without mistakes
            print('Succsess')
            break # Die x_x
        else:
            print('Error')
            break
    
