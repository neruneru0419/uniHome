import speech_recognition as sr


def mic():
    record = sr.Recognizer()
    mic = sr.Microphone()
    with mic as source:
        record.adjust_for_ambient_noise(source)
        audio = record.listen(source)
    #record.energy_threshold = 300
    try:
        words = record.recognize_google(audio, language='ja-JP')
    except:
        words = ""
    isGreeting = (words == "おはよう" or words == "おやすみ" or words == "ただいま")
    print(words)
    return isGreeting
