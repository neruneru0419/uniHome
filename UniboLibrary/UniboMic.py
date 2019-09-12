import speech_recognition as sr
def mic():
    record = sr.Recognizer()
    mic = sr.Microphone()
    isGreeting = False
    with mic as source:
        record.adjust_for_ambient_noise(source)
        audio = record.listen(source)

    words = record.recognize_google(audio, language='ja-JP')
    if (isGreeting == "おはよう" or isGreeting == "おやすみ" or isGreeting == "ただいま"):
        isGreeting = True
    return words, isGreeting