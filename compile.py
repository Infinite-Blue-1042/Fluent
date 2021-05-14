# compile.py
# Run on current file with rOS
# Token '#*#' means line for testing purposes.

from tkinter import *


def error(length):
    if len(param) != length:
        raise RuntimeError


__author__ = 'Aarav Dave'
__file__ = 'code.fl'  #*#

variables = {}

with open(__file__) as file:
    for line in file:
        if not line.strip() or line.startswith('//'):
            continue

        command, *param = line.strip().split()
        if command == 'window':
            command, param = param[0], param[1:]
            if command == 'create':
                error(1)
                variables[param[0]] = Tk()
                variables[param[0]].title('app')
            elif command == 'rename':
                error(2)
                variables[param[0]].title(' '.join(param[1:]))
            elif command == 'size':
                error(3)
                variables[param[0]].geometry(f'{param[1]}x{param[2]}')
            elif command == 'run':
                error(1)
                variables[param[0]].mainloop()
            else:
                error(-1)
        else:
            error(-1)
