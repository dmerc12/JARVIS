from settings import settings
import speech_recognition
import pyttsx4

# Engine for speach to text
engine = pyttsx4.init(settings.voice)

# Sets voice properties
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
engine.setProperty('rate', settings.rate)

# Speak function
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

# Take command
def takeCommand():
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

# Main function for running JARVIS
if __name__ == '__main__':
    # Infinite loop to have JARVIS running while program is running
    while True:
        # Listen for command and return command
        query = takeCommand().lower()
        # Respond to name
        if 'jarvis' in query:
            response = 'Yes sir'
            print(response)
            speak(response)
        # Respond to question 'who are you?'
        elif 'who are you' in query:
            response = 'My name is JARVIS. I am an artificial intelligence built to assist you with day to day tasks. Please let me know if there is anything I can do to be of assistance sir'
            print(response)
            speak(response)

