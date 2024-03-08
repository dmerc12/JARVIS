from settings import settings
import pyttsx4

# Engine for speach to text
engine = pyttsx4.init(settings.voice)

# Sets voice properties
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
engine.setProperty('rate', settings.rate)
