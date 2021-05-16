# compile.py
# Run on current file with rOS
# Token '#*#' means line for testing purposes.

from tkinter import *
import sys


def check_error(length, equal=True):
    if (len(param) != length and equal) or (len(param) < length and not equal):
        raise RuntimeError


def line_error():
    quit(f'Error on Line _:\n{line}')


__author__ = 'Aarav Dave'
if sys.argv[1:]:
    __file__ = sys.argv[1]
else:
    __file__ = 'code.fl'

vars = {}
with open(__file__) as file:
    for line in file:
        if not line.strip() or line.startswith('//'):
            continue

        command, *param = line.strip().split()
        if command == 'window':
            command, param = param[0], param[1:]
            if command == 'create':
                check_error(1)
                vars[param[0]] = Tk()
                vars[param[0]].title('app')
            elif command == 'rename':
                check_error(2, False)
                vars[param[0]].title(' '.join(param[1:]))
            elif command == 'resize' or command == 'size':
                check_error(3)
                vars[param[0]].geometry(f'{param[1]}x{param[2]}')
            elif command == 'run':
                check_error(1)
                vars[param[0]].mainloop()
            else:
                line_error()
        elif command == 'place':
            check_error(1, False)
            values = {'x': 0, 'y': 0, 'width': 50, 'height': 50}
            for value in param[1:]:
                value = value.split('=')
                values[value[0]] = value[1]
            vars[param[0]].place(x=int(values['x']), y=int(values['y']), width=int(values['width']), height=int(values['height']))
        elif command == 'button':
            command, param = param[0], param[1:]
            if command == 'create':
                check_error(2)
                vars[param[1]] = Button(vars[param[0]])
        elif command == 'entry':
            command, param = param[0], param[1:]
            if command == 'create':
                check_error(2)
                vars[param[1]] = Text(vars[param[0]])
        else:
            line_error()
