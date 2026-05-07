import os
import logging
from datetime import datetime

class ProjektLogger:
    def __init__(self):
        # Jelenlegi fájl helye (utils mappa)
        current_dir = os.path.dirname(os.path.abspath(__file__))

        # Kilépés a projekt gyökerébe
        project_root = os.path.abspath(os.path.join(current_dir, ".."))

        # Log mappa a projekt gyökerében
        log_dir = os.path.join(project_root, "log")
        os.makedirs(log_dir, exist_ok=True)

        # Dátum alapú logfájlnév
        date_str = datetime.now().strftime("%Y%m%d")
        log_filename = f"G86X1Y_OOP_B_feladat_{date_str}.log"
        log_path = os.path.join(log_dir, log_filename)

        # Logger beállítása
        self.logger = logging.getLogger("ProjektLogger")
        self.logger.setLevel(logging.DEBUG)

        if not self.logger.handlers:
            file_handler = logging.FileHandler(log_path, encoding='utf-8')
            formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
            file_handler.setFormatter(formatter)
            self.logger.addHandler(file_handler)


    def debug(self, message):
        self.logger.debug(message)

    def debugprint(self, message):
        print(message)
        self.logger.debug(message)

    def info(self, message):
        self.logger.info(message)
    
    def infoprint(self, message):
        print(message)
        self.logger.info(message)

    def warning(self, message):
        self.logger.warning(message)

    def warningprint(self, message):
        print("\033[93m {}\033[00m".format(message))
        self.logger.warning(message)

    def error(self, message):
        self.logger.error(message)

    def errorprint(self, message):
        print("\033[91m {}\033[00m".format(message))
        self.logger.error(message)
