import speech_recognition as sr


def mic():
    record = sr.Recognizer()
    mic = sr.Microphone()
    isGreeting = False
    with mic as source:
        record.adjust_for_ambient_noise(source)
        audio = record.listen(source)
    try:
        words = record.recognize_google(audio, language='ja-JP')
    except:
        words = ""
    if (words == "おはよう" or words == "おやすみ" or words == "ただいま"):
        isGreeting = True
    print(words)
    return isGreeting