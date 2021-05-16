# compile.py
# Run on current file with rOS
# Token '#*#' means line for testing purposes.

from tkinter import *
import sys
import re

class ParsingError(Exception):
    pass

def line_error(line):
    raise ParsingError(f'Error on Line:\n{line}')

def check_error(length, line, equal=True):
    if (len(param) != length and equal) or (len(param) < length and not equal):
        raise ParsingError(f'Error on Line:\n{line}')


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
        
        # This line finds the comments using regex and the python re module
        comments = re.findall("(\/\*[\w\'\s\r\n\*]*\*\/)|(\/\/[\w\s\']*)", line)
        if comments:
            for comment in comments:
                for part in comment:
                    if part:
                        line = line.replace(part, "")


        command, *param = line.strip().split()
        if command == 'window':
            command, param = param[0], param[1:]
            if command == 'create':
                check_error(1, line)
                vars[param[0]] = Tk()
                vars[param[0]].title('app')
            elif command == 'rename':
                check_error(2, line, False)
                vars[param[0]].title(' '.join(param[1:]))
            elif command == 'resize' or command == 'size':
                check_error(3, line)
                vars[param[0]].geometry(f'{param[1]}x{param[2]}')
            elif command == 'not_resizable':
                check_error(2, line)
                if param[1] == "both":
                    vars[param[0]].resizable(False, False)
                elif param[1] == "x":
                    vars[param[0]].resizable(False, True)
                elif param[1] == "y":
                    vars[param[0]].resizable(True, False)
            elif command == 'run':
                check_error(1, line)
                vars[param[0]].mainloop()
            else:
                line_error(line)
        elif command == 'place':
            check_error(1, line, False)
            values = {'x': 0, 'y': 0, 'width': 50, 'height': 50}
            for value in param[1:]:
                value = value.split('=')
                values[value[0]] = value[1]
            vars[param[0]].place(x=int(values['x']), y=int(values['y']), width=int(values['width']), height=int(values['height']))
        elif command == 'button':
            command, param = param[0], param[1:]
            if command == 'create':
                check_error(2, line)
                vars[param[1]] = Button(vars[param[0]])
            else:
                line_error(line)
        elif command == 'entry':
            command, param = param[0], param[1:]
            if command == 'create':
                check_error(2, line)
                vars[param[1]] = Text(vars[param[0]])
            else:
                line_error(line)
        else:
            line_error(line)
