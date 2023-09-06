import speech_recognition as s_rec
print("hi whatsapp my self ARYAVIR and iam developed by sanskar")
sr = s_rec.Recognizer()

print("I am listening.....................")

with s_rec.Microphone() as mc:
    audio = sr.listen(mc)
    query = sr.recognize_google(audio, language='eng-in')
    print("printing")
    print(query)
