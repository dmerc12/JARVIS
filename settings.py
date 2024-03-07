import platform

# Settings for speach engine
class Settings:

    def __init__(self):
        if platform.system() == 'Windows':
            self.voice = 'sapi5'
        else:
            self.voice = 'nsss'
        self.rate = 250
        self.language = 'en-US'

# Instantiating settings
settings = Settings()
