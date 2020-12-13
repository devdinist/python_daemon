import logging
import os
import signal
import sys
import time


class Say:
    SIG = {
        2: "인터럽트",
        9: "강제종료",
        15: "종료요청"
    }

    def __init__(self, arg):
        logging.basicConfig(level=logging.INFO, format='%(message)s')
        self.logger = logging.getLogger("Say")

        self.ment = arg.Say
        self.sleep = arg.Sleep
        self.logname = arg.log
        self.worker = True

        self.logfile = logging.FileHandler(self.logname)
        self.logger.addHandler(self.logfile)

        signal.signal(signal.SIGINT, self.sig_handler)
        #signal.signal(signal.SIGKILL, self.sig_handler)
        signal.signal(signal.SIGTERM, self.sig_handler)

    def player(self):
        self.logger.info("이 프로세스의 현재 PID는 {0}입니다.".format(os.getpid()))
        count = 0
        while self.worker:
            self.logger.info("{0}(이)라고 {1}번째 외칩니다.".format(self.ment, count))
            count += 1
            time.sleep(int(self.sleep))

    def sig_handler(self, sig_number, frame):
        self.logger.info("{0} 발생으로 프로그램이 종료되었습니다.".format(self.SIG[sig_number]))
        sys.exit(sig_number)
