import speech_recognition as sr
import pyaudio
import os
import sys

def open_app(command):
    if "open browser" in command:
        print("Opening Firefox...")
        os.system('start firefox')
    elif "open media player" in command:
        print("Opening Windows Media Player...")
        os.system('start wmplayer')
    else:
        print("Command not recognized.")

def main():
    recognizer = sr.Recognizer()
    mic = sr.Microphone()

    print("Say 'open browser' or 'open media player'...")

    while True:
        with mic as source:
            recognizer.adjust_for_ambient_noise(source)
            print("Listening for command...")
            audio = recognizer.listen(source)
        try:
            command = recognizer.recognize_google(audio).lower()
            print("You said:", command)
            open_app(command)
            # Uncomment next line to exit after a successful command
            # sys.exit()
        except sr.UnknownValueError:
            print("Sorry, could not understand audio. Try again.")
        except sr.RequestError as e:
            print(f"Speech recognition error: {e}")
            break

if __name__ == "__main__":
    main()
