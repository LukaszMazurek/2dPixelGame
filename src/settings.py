import logging

from pathlib import Path


class Settings(object):
    caption = "SwordOfDestiny"
    display_size = (720, 480)
    height_threshold = 0.2
    frame_rate = 14
    logger = None

    @staticmethod
    def get_ground_height() -> int:
        return int(Settings.display_size[1] * Settings.height_threshold)

    @staticmethod
    def get_ground_width() -> int:
        return Settings.display_size[0]

    @staticmethod
    def set_logger():
        logger = logging.getLogger('pygame-logger')
        logger.setLevel(logging.DEBUG)
        fh = logging.FileHandler(Path('src/logs/logs.log'))
        fh.setLevel(logging.DEBUG)
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
        fh.setFormatter(formatter)
        logger.addHandler(fh)
        return logger

