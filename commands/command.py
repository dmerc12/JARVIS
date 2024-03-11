import speech_recognition
from .speak import speak

# Function for taking a command
def take_command():
    # Listen to command
    recognizer = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source:
        print('Listening...')
        recognizer.pause_threshold = 1
        audio = recognizer.listen(source)
    # Recognize command
    try:
        print('Thinking...')
        query = recognizer.recognize_google(audio, language='en-US')
        print(f'You said: {query}\n')
    # Handling if command is not recognized
    except Exception as e:
        response = "I'm sorry, could you please say that again?"
        print(response)
        speak(response)
        return 'None'
    # Return query
    return query

# Function for listening for name
def listen_for_name():
    # Listen for name
    recognizer = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source:
        print('Waiting to be called...')
        recognizer.pause_threshold = 1
        audio = recognizer.listen(source)
    # Recognize what is spoken
    try:
        query = recognizer.recognize_google(audio, language='en-US')
        if 'jarvis' in query.lower():
            return True
    # Handling any exceptions that may occur
    except Exception as e:
        return False
    # Return query
    return False
