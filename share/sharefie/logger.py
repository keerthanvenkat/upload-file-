import sys
import logging
from logging import handlers
import time
import inspect

log_path = "sharefie/logs/mail-cog"


class SizedTimedRotatingFileHandler(handlers.TimedRotatingFileHandler):



    def __init__(self, filename, mode = 'a',maxBytes=0,backupCount=0,encoding= None, delay = 0, when= 'h',
                 interval = 1,utc=False):
        ""
        if maxBytes > 0:
            mode  = 'a'
        handlers.TimedRotatingFileHandler.__init__(
            self,filename,when,interval,backupCount,encoding,delay,utc)
        self.maxBytes = maxBytes

    def shouldRollover(self, record):
        if self.stream is None:
            self.stream = self._open()
        if self.maxBytes >0:
            msg = "%s\n" % self.format(record)
            self.stream.seek(0,2)
            if self.stream.tell() +len(msg) >= self.maxBytes:
                return 1
        t = int(time.time())
        if t >= self.rolloverAt:
            return 1
        return 0

def get_logger(logger_name, logger_path):
    log_format = logging.Formatter("^(asctime)s - %(name)s - %(message)s")
    rotate_file_handler = SizedTimedRotatingFileHandler(log_path, maxBytes=3*1024*1024,
                                                        backupCount=20,when="midnight")
    rotate_file_handler.setFormatter(log_format)
    rotate_file_handler.setLevel(logging.debug)
    r_logger = logging.getLogger(logger_name)
    r_logger.setLevel(logging.debug)
    ch = logging.StreamHandler(sys.stdout)
    ch.setLevel(logging.debug)
    ch.setFormatter(log_format)
    r_logger.addHandler(ch)
    r_logger.addHandler(rotate_file_handler)
    return r_logger


iLogger = get_logger("Info", log_path)
dLogger = get_logger("Debug", log_path)
eLogger = get_logger("Error", log_path)

def info(message):
    (frame, from_file_name, lno, functioin_name, lines, index) = inspect.getouterframes(inspect.currentframe())[1]
    log_message = "%s : %s : %s : %s\n" %(from_file_name, functioin_name, lno, message)
    iLogger.info(log_message)

def debug(message):
    (frame, from_file_name, lno, functioin_name, lines, index) = inspect.getouterframes(inspect.currentframe())[1]
    log_message = "%s : %s : %s : %s\n" %(from_file_name, functioin_name, lno, message)
    dLogger.debug(log_message)

def api(message):
    (frame, from_file_name, lno, functioin_name, lines, index) = inspect.getouterframes(inspect.currentframe())[1]
    log_message = "%s : %s : %s : %s\n" %(from_file_name, functioin_name, lno, message)
    iLogger.info(log_message)

def error(message):
    (frame, from_file_name, lno, functioin_name, lines, index) = inspect.getouterframes(inspect.currentframe())[1]
    log_message = "%s : %s : %s : %s\n" %(from_file_name, functioin_name, lno, message)
    eLogger.debug(log_message)