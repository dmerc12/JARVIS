from .greeting import greeting
import speech_recognition
from .speak import speak

# Function for taking a command
def take_command():
    # Listen to command
    recognizer = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source:
        print('Listening...', flush=True)
        recognizer.pause_threshold = 1
        try:
            audio = recognizer.listen(source, timeout=5)
        except speech_recognition.WaitTimeoutError:
            return 'nothing heard'
    # Recognize command
    try:
        print('Thinking...')
        query = recognizer.recognize_google(audio, language='en-US')
        print(f'You said: {query}\n', flush=True)
    # Handling if command is not recognized
    except Exception as e:
        response = "I'm sorry, could you please say that again?"
        print(response, flush=True)
        speak(response)
        return 'None'
    # Return query
    return query

# Function for listening for name
def listen_for_name():
    # Listen for name
    recognizer = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source:
        print('Waiting to be called...', flush=True)
        recognizer.pause_threshold = 1
        try:
            audio = recognizer.listen(source, timeout=2)
        except speech_recognition.WaitTimeoutError:
            pass
    # Recognize what is spoken
    try:
        triggers = ['jarvis', 'are you there']
        query = recognizer.recognize_google(audio, language='en-US').lower()
        if any(trigger in query for trigger in triggers):
            greeting()
            return True
    # Handling any exceptions that may occur
    except Exception as e:
        return False
    # Return false if no trigger command detected
    return False
