import sys
import os
import time


def deamonize(stdin='/dev/null', stdout='/dev/null', stderr='/dev/null'):
    try:
        pid = os.fork()
        if pid > 0:
            sys.exit(0)
    except OSError as error:
        sys.stderr.write('_Fork #1 failed: {0} \n'.format(error))
        sys.exit(1)

    os.chdir('/')
    os.umask(0)
    os.setsid()

    try:
        pid = os.fork()
        if pid > 0:
            sys.exit(0)
    except OSError as err:
        sys.stderr.write(f'_Fork #2 failed:{err}\n')
        sys.exit(1)

    sys.stdout.flush()
    sys.stdout.flush()

    si = open(stdin, 'r')
    so = open(stdout, 'a+')
    se = open(stderr, 'w')

    os.dup2(si.fileno(), sys.stdin.fileno())
    os.dup2(so.fileno(), sys.stdout.fileno())
    os.dup2(se.fileno(), sys.stderr.fileno())


def test():
    sys.stdout.write(f"Daemon started with pid {os.getpid()}")
    while True:
        now = time.strftime('%X', time.localtime())
        sys.stdout.write(f'{time.ctime()}\n')
        sys.stdout.flush()
        time.sleep(1)


if __name__ == '__main__':
    deamonize('/dev/null', '/Users/xiawang/Desktop/Python005-01/week01/d2.log', '/dev/null')
    test()
