import sys, os, argparse
from Say import Say

if __name__ == '__main__':
    par = argparse.ArgumentParser()
    par.add_argument("-Say",help="enter say",default="hello")
    par.add_argument("-Sleep",help="enter sleep time",default=1)
    par.add_argument("-log", help="enter log file eg)log.log", required=True)
    args = par.parse_args()

    pid = os.fork()
    if pid > 0:
        exit(0)
    else:
        os.chdir("/")
        os.setsid()
        os.umask(0)

        pid = os.fork()
        if pid > 0:
            exit(0)
        else:
            sys.stdin.flush()
            sys.stdout.flush()

            si = open(os.devnull, 'r')
            so = open(os.devnull, 'a+')
            se = open(os.devnull, 'a+')

            os.dup2(si.fileno(), sys.stdin.fileno())
            os.dup2(so.fileno(), sys.stdout.fileno())
            os.dup2(se.fileno(), sys.stderr.fileno())

            with open("/var/run/forker.pid","w") as write:
                write.write(str(os.getpid()))

            tell = Say(args)
            tell.player()
