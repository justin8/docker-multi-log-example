import time
import logging
from logging.handlers import RotatingFileHandler
formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')

# Logger will rotate files every 300 bytes and keep 10 files
# This lets us test regular rotation of the files and ensure that we are logging this correctly
def setup_logger(name, log_file, level=logging.INFO):
    """To setup as many loggers as you want"""

    # handler = logging.FileHandler(log_file)        
    handler = RotatingFileHandler(log_file, 'a', 300, 10)
    handler.setFormatter(formatter)

    logger = logging.getLogger(name)
    logger.setLevel(level)
    logger.addHandler(handler)

    return logger


first_logger = setup_logger('first_logger', '/logs/first_logfile.log')
second_logger = setup_logger('second_logger', '/logs/second_logfile.log')

for i in range(0, 100000000):
    first_logger.info(f"Logging message {i} to first logger")
    second_logger.info(f"Logging message {i} to second logger")
    print(f"Emitted log message {i} to the log files...")
    time.sleep(1)