
def parse_sys_args(args):
    d = {}
    for arg in args:
        spliter_pos = arg.find('=')
        if (spliter_pos != -1):
            d[arg[:spliter_pos]] = arg[spliter_pos+1:]
    return d
