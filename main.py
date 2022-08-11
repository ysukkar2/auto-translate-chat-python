from gettext import translation
from googletrans import Translator
translator = Translator()
text = "Ich bin ein programmierer"
translation = translator.translate(text,src="de",dest="en")
print(translation.text)