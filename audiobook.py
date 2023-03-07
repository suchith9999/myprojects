from gtts import gTTS
import os

# Enter the text you want to convert to speech
text = "Hello, how are you today? your text here"

# Choose the language and create the audio object
language = 'en'
speech = gTTS(text=text, lang=language, slow=False)

# Save the audio file as an MP3 and play it
speech.save("audio.mp3")
os.system("mpg123 audio.mp3")



