"""
Run a python script, adding extra directories to the python path.
"""


def main(args):
    def usage():
        print >>sys.stderr, "pythonpath.py -I directory script.py [args...]"
        sys.exit(150)

    paths = []

    while True:
        try:
            arg = args[0]
        except IndexError:
            usage()

        if arg == '-I':
            args.pop(0)
            try:
                path = args.pop(0)
            except IndexError:
                usage()

            paths.append(path)
            continue

        if arg.startswith('-I'):
            paths.append(args.pop(0)[2:])
            continue

        break

    script = args[0]

    sys.path[0:0] = [os.path.dirname(script)] + paths
    sys.argv = args
    sys.argc = len(args)

    frozenglobals['__name__'] = '__main__'
    frozenglobals['__file__'] = script

    execfile(script, frozenglobals)

# Freeze scope here ... why this makes things work I have no idea ...
frozenglobals = globals()

import sys, os

if __name__ == '__main__':
    main(sys.argv[1:])
