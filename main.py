import speech_recognition as sr
from pydub import AudioSegment
import os
from dotenv import load_dotenv

load_dotenv()

CREDENTIALS_PATH = os.getenv('GOOGLE_APPLICATION_CREDENTIALS')
AUDIO_NAME = os.getenv('AUDIO_NAME')
AUDIO_EXTENSION = os.getenv('AUDIO_EXTENSION')
AUDIO_LANGUAGE = os.getenv('AUDIO_LANGUAGE')


with open(CREDENTIALS_PATH, 'r') as file:
    CREDENTIALS = file.read()


def get_next_filename(base_name, extension):
    i = 0
    while True:
        i += 1
        filename = f"{base_name}_{i}.{extension}"
        if not os.path.exists(filename):
            return filename


def convert_audio_to_wav(audio):
    os.path.exists('audio.wav') and os.remove('audio.wav')
    audio = AudioSegment.from_file(audio)
    audio.export("audio.wav", format="wav")

    return "audio.wav"


def main():
    sound = convert_audio_to_wav(f"{AUDIO_NAME}.{AUDIO_EXTENSION}")
    r = sr.Recognizer()
    with sr.AudioFile(sound) as source:
        r.adjust_for_ambient_noise(source)
        print("Convirtiendo Audio a Texto...")
        audio = r.listen(source)

        try:
            text = r.recognize_google_cloud(audio, credentials_json=CREDENTIALS_PATH, language=AUDIO_LANGUAGE)
            print("Texto: " + text)
            base_name = 'output'
            if os.path.exists(f"{base_name}.txt"):
                filename = get_next_filename(base_name, 'txt')
            else:
                filename = f"{base_name}.txt"

            with open(filename, 'w', encoding='utf-8') as file:
                file.write(text)

            print(f"Texto guardado en {filename}")
        except Exception as e:
            print("Error: " + str(e))


if __name__ == "__main__":
    main()
