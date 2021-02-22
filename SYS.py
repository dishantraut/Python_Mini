"""
# sys module
    provides functions and variables 
    used to manipulate 
    different parts of the 
    Python runtime environment.

# sys.argv 
    returns a list of command line arguments passed to a Python script. 
    The item at index 0 in this list is always the name of the script. 
    The rest of the arguments are stored at the subsequent indices.

# sys.path
    is an environment variable that is a search path for all Python modules.

# sys.version
    attribute displays a string containing the version number of the current Python interpreter.

# stdout and stdin
    we can pass messages and errors through to the command line, or just use it for logging purposes.
"""
import sys
print("\nYou entered: ",sys.argv[1], sys.argv[2], sys.argv[3])
print("\nPath = ",sys.path)
print("\nExit = ",sys.exit)
print("\nVersion = ",sys.version)

def main(arg):
    print("\nMain Function = ",arg)

main(sys.argv[1])

sys.stderr.write('\nThis is stderr text\n')
sys.stderr.flush()
sys.stdout.write('\nThis is stdout text\n')
