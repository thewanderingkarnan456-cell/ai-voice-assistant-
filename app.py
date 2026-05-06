import streamlit as st
import speech_recognition as sr
import pyttsx3

engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

st.title("🎙️ AI Voice Assistant")

if st.button("Speak"):
    r = sr.Recognizer()
    with sr.Microphone() as source:
        st.write("Listening...")
        audio = r.listen(source)

    try:
        command = r.recognize_google(audio)
        st.write("You said:", command)

        if "hello" in command:
            response = "Hello, how can I help you?"
        elif "time" in command:
            import datetime
            response = str(datetime.datetime.now().time())
        else:
            response = "I don't understand"

        st.write("AI:", response)
        speak(response)

    except:
        st.write("Error recognizing voice")
