import speech_recognition as sr
from time import sleep

def recog_speech_text():

    speech_recog = sr.Recognizer()
    microphone = sr.Microphone()

    write_flag = False
    recog_words = []
    recog_tmp_word = ''
    while True:
        if recog_tmp_word == 'стоп':
            print("[INFO] Finishing writing words...")
            result_words = [word for word in recog_words if word != '']
            return result_words
        elif recog_tmp_word == 'старт':
            write_flag = True
            print('[INFO] Starting writing words...')
        if write_flag and recog_tmp_word != 'старт':
            recog_words.append(recog_tmp_word)

        with microphone as source:
            audio = speech_recog.listen(source)                  # catch input of microphone
            # then send to Google recognizer
            try:
                recog_tmp_word = speech_recog.recognize_google(audio, language = 'uk-UA')
            except sr.exceptions.UnknownValueError:
                recog_tmp_word = ''
                continue
            # for below conditions(some words recognizing wit Uppercase)
            recog_tmp_word = recog_tmp_word.lower()
            print(recog_tmp_word)
# testing
if __name__ == '__main__':
    your_words = recog_speech_text()
    print(your_words)
