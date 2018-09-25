__author__ = "Martin Maiksnar"

import sys

def arguments_handling():
    arg_len = len(sys.argv)
    log_file = sys.argv[1]
    return(arg_len,log_file)

print(arguments_handling())

#print("number of arguments: ",arg_len, "arguments")
#print("argument list", str(sys.argv))

press_key = input("Press any key to continue")

#OPT-TRAN-24-08-2018-12-33-37.xml
#OPT-MSG-24-08-2018-12-33-37.txt
#TME-PACKET-24-08-2018-12-33-38.txt
#RepsolOPTConfiguration.xml
