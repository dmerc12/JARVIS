from .speak import speak

# Function to stop JARVIS
def stop_jarvis():
    response = 'Yes sir, shutting down. Goodbye'
    print(response)
    speak(response)
    exit()
    