from fileinput import filename
import speech_recognition as sr

from pydub import AudioSegment
from pydub.silence import split_on_silence
from getTranslation import googleTranslation

r = sr.Recognizer()

def silence_based_video(path, lang):
    audio_file = AudioSegment.from_wav(path)
    text_file = open("recognized.txt", "w", encoding="utf-8")
    translated_text_file = open("recognized_and_translated.txt", "w", encoding="utf-8")
    chunks = split_on_silence(audio_file, min_silence_len=1000, silence_thresh= -40)
    i = 0
    for chunk in chunks:
      #  chunk_silent = AudioSegment.silent(duration=3)
     #   audio_chunk = chunk_silent + chunk + chunk_silent
        chunk.export("./chunk{0}.wav".format(i), bitrate ='192k', format ="wav")
        filename = 'chunk'+str(i)+'.wav'
        with sr.AudioFile(filename) as source:
           # r.adjust_for_ambient_noise(source)
            audio_listened = r.listen(source)
            rec = r.recognize_google(audio_listened, language=lang)
            text_file.write(rec+". ")
            translated_text_file.write(googleTranslation(rec, 'en', 'ru')+". ")
    return "Successfully recognized and translated"
silence_based_video("audio.wav", 'en-EN')
