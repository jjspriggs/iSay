# iSay by GoDzM4TT3O, created in Pythonista 3
# Works with both Python 2 and 3. Only uses 7 lines of code!
import speech, console
lang = console.input_alert("iSay by GoDzM4TT3O", "Type a language you'd like your phone to speak in (get a list of languages by typing langs)\nExample:\nif my phone will speak in American English, I will type en-US.")
if lang == 'langs':
	console.alert("iSay by GoDzM4TT3O", "Here is a list of languages:\n" + "\n".join(sorted(speech.get_recognition_languages())))
text = console.input_alert("iSay by GoDzM4TT3O", "Now type something and your phone will say it in this language: " + lang)
speech.say(text, lang)
console.alert("iSay by GoDzM4TT3O", "Text:\n" + text)
