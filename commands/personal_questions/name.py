from ..utils.speak import speak

def speak_name():
    response = 'My name is JARVIS. I am an artificial intelligence built to assist you with day to day tasks.\nPlease let me know if there is anything I can do to be of assistance sir!'
    print(response, flush=True)
    speak(response)
