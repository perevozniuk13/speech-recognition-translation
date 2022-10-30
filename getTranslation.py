import googletrans 
from googletrans import Translator
import speech_recognition

def googleTranslation(sentence, fromLan=None, toLan='en'):
    translator = Translator()
    if fromLan==None:
        d = translator.detect(sentence)
        fromLan = d.lang
    result = translator.translate(sentence, src=fromLan, dest=toLan)
    return result.text
