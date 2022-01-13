import speech_recognition as sr
import pyttsx3
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def stt():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("JARVIS listening...")
        audio = r.listen(source)
    
    try:
        query = r.recognize_google(audio)
        print(f"master:{query}")
        return query
    
    except:
        print("I did not hear you. Try again.")

def main():
    stt()
main()
