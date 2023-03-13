import os
import logging
from logging.handlers import TimedRotatingFileHandler
import datetime

# create logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

ROOT_DIR = os.path.abspath(os.curdir)

# log dir
log_dir = os.path.join(ROOT_DIR, 'logs')
# Create logs folder if not exist
if not os.path.exists(log_dir):

    # if the demo_folder directory is not present
    # then create it.
    os.makedirs(log_dir)

print(log_dir)

# create TimedRotatingFileHandler
# log_filename = datetime.datetime.now().strftime('myapp-%Y-%m.log')
log_filename = os.path.join(
    log_dir, datetime.datetime.now().strftime('myapp-%Y-%m.log'))
handler = TimedRotatingFileHandler(
    log_filename, when='midnight', interval=1, backupCount=0)
handler.setLevel(logging.INFO)

# create formatter and add to handler
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)

# add handler to logger
logger.addHandler(handler)

# test logging
logger.info('This is a test log message')
