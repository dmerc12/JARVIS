from engine import engine

# Speak function
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
