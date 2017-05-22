import sys
import parser
import os

# 1
import services.parser.list_parser as p
# 2
import services.parser.list_parser
# 3
from services.parser.list_parser import parse_sys_args
# 4
import services.parser
# 5
import services

if __name__ == '__main__':
    print(sys.argv)
    print(sys.argv[1])

    if(sys.argv[1] == '1'):
        print('parser.list_parser as p')
        output = p.parse_sys_args(sys.argv)
    if(sys.argv[1] == '2'):
        print('parser.list_parser')
        output = parser.list_parser.parse_sys_args(sys.argv)
    if(sys.argv[1] == '3'):
        print('from parser.list_parser import parse_sys_args')
        output = parse_sys_args(sys.argv)

    '''
    avec les __init__.py
    '''

    if(sys.argv[1] == '4'):
        print('import parser avec le __init__.py')
        output = services.parser.parse_sys_args(sys.argv)
    if(sys.argv[1] == '5'):
        print('import services avec le __init__.py')
        output = services.parse_sys_args(sys.argv)

    # output = services.parser.list_parser.parse_sys_args(sys.argv)

    os.system("pwd")
    print(output)

    conf_argument = output.pop("conf")
    print(conf_argument)
    print(output)
