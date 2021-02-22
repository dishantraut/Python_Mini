"""
# SubProcess Module
    Invoking internal or external commands of the operating system as well as 
    starting any other application available in the system can be achieved with 
    the help of certain functions defined in two built-in modules - os module and subprocess module

# subprocess.run() 
    runs the command in the string argument, waits for the process to complete, and object of CompletedProcess class

# subprocess.call()
    function is a part of older version of this module (before Python 3.5). 
    This is similar to the run() function, but returns returncode attribute.

"""
import subprocess
print("\nRun = ",subprocess.run("dir *.txt", shell=True))
print("\nReturnCode = ",subprocess.call("whoami", shell=True))
