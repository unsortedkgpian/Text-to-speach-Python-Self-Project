import gtts
import playsound

text = input("enter something here: ")

sound = gtts.gTTS(text, lang="en")

sound.save("Welcome.mp3")

playsound.playsound("Welcome.mp3")
