from ..speak import speak

# Funciton for auto response
def default():
    greeting = 'Yes, sir? How may I be of assistance?'
    print(greeting)
    speak(greeting)
