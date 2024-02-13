import pyttsx3

class TextToSpeech:
    engine: pyttsx3.Engine

    def __init__(self, voice, rate: int , volume: float):
        self.engine = pyttsx3.init()
        if voice:
            self.engine.setProperty('voice', voice)
        self.engine.setProperty('rate', rate)
        self.engine.setProperty('volume', volume)

    def list_available_voices(self):
        voices: list = [self.engine.getProperty('voices')]

        for i, voice in enumerate(voices[0]):
            print(f'{i + 1} {voice.age}: {voice.languages[0]} ({voice.gender}) [{voice.id}]')

    def text_to_speech(self, text: str, save: bool = False, file_name='output.mp3'):
        self.engine.say(text)
        print('I am Speaking...')

        if save:
            self.engine.save_to_file(text, file_name)

        self.engine.runAndWait()
# english
if __name__ == '__main__':
    tts = TextToSpeech('aragonese', 200, 1.0)
    tts.list_available_voices()
    tts.text_to_speech('Hello there ! This is aditya')