

class Settings(object):
    caption = "SwordOfDestiny"
    display_size = (720, 480)
    height_threshold = 0.2
    frame_rate = 14

    @staticmethod
    def get_ground_height() -> int:
        return int(Settings.display_size[1] * Settings.height_threshold)

    @staticmethod
    def get_ground_width() -> int:
        return Settings.display_size[0]
