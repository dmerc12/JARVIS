from .speak import speak
import sys
import os

# Function to stop JARVIS
def stop_jarvis():
    response = 'Yes sir, shutting down. Goodbye'
    print(response, flush=True)
    speak(response)
    exit()

# Function to restart JARVIS
def restart_jarvis():
    response = 'Yes sir, refreshing my system now.\nOne moment please...'
    print(response, flush=True)
    speak(response)
    os.execl(sys.executable, f'"{sys.executable}"', *sys.argv)
