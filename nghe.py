import speech_recognition

# Initialize the recognizer
robot_ear = speech_recognition.Recognizer()
with speech_recognition.Microphone() as mic:
    print("Robot: I'm listening")
    audio = robot_ear.listen(mic)
