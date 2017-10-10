import os
import sys
import mode

argment = sys.argv
arg_dict = {
        1:'connect',
        2:'add',
        3:'remove',
        4:'exit'
        }

if len(argment) == 1:
    selected_mode = mode.mode_select()
    print(selected_mode)
    argment.append(arg_dict[selected_mode])

if argment[1] == 'connect':
    mode.connect()
elif argment[1] == 'add':
    pass
elif argment[1] == 'remove':
    pass
elif argment[1] == 'exit':
    mode.exit()
else:
    print(argment[1],'は不正な引数です。')
