from commands.take_command import take_command
from commands.speak import speak

# Main function for running JARVIS
if __name__ == '__main__':
    # Infinite loop to have JARVIS running while program is running
    while True:
        # Listen for command and return command
        query = take_command().lower()
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
