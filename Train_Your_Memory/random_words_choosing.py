import random
from gtts import gTTS
import subprocess as sp
from mutagen.mp3 import MP3  # Py-lib - mutagen - for handling with metadata of audiofile
import reconizing_my_speech as speech
from time import sleep

filename = 'UA_words.txt'
def choose_noun_words(file = filename, words_amount = 10):
    result_words = []
    with open(file, 'rt') as read_nouns:
        nouns_list = []
        for noun in read_nouns:
            nouns_list.append(noun[:-1])

        # choose random words
        len_list = len(nouns_list)
        print("Words for practice:\n")
        while words_amount > 0:
            rand_word = nouns_list[random.randint(0, len_list - 1)]
            # for exclude duplicated words.
            if rand_word in result_words:
                continue
            else:
                result_words.append(rand_word)
                words_amount -= 1

    return result_words

#writing audiofile with these words
def write_audiofile(words = ['test'], filename = 'test.mp3'):
    pause_between_words = ' ' * 250  # not very effective but it almost works.
    speech_string = pause_between_words.join(words)
    # A title of exercise
    audio_text = 'Старт через 3 ' + ' ' * 30 + '2' + ' ' * 30 + '1' + ' ' * 60
    audio_text += speech_string
    audio_text += ' ' * 200 + 'Тепер повторіть слова.'
    audio_speech = gTTS(audio_text, lang = 'uk', slow = True)

    # saving into mp3 file
    audio_speech.save(filename)

#starting audiofile for training(on Linux using player Audacious)
def start_audio(audiofile = ''):
    if audiofile == '':
        return 'No input audio.'
    else:
        proc = sp.run(['audacious', audiofile])

        audiofile = MP3(audiofile)
        return audiofile.info.length  # return audio duration in seconds


def result_prog(amount_words = 10):
    words_for_training = choose_noun_words(filename, amount_words)

    write_audiofile(words_for_training, 'words_for_training.mp3')

    audio_length = start_audio('words_for_training.mp3')

    sleep(audio_length)  #suspending program.

    # get recognition words list. Last element - is a flag(stop-word).
    recog_words = speech.recog_speech_text()
    # if amount of your words more than started words, saving only first required words.
    if len(recog_words) > amount_words:
        recog_words = recog_words[:amount_words]

    print('Your words:', recog_words[:-1])
    print(words_for_training)
    print('=' * 60)
    # show your mark - how much you remember words in right order.
    check_words(words_for_training, recog_words[:-1])

# checking for right words in right order
def check_words(start_words = ['text'], your_words = ['null']):
    result_mark = 0
    amount_words = len(start_words)
    for i in range(len(your_words)):
        if your_words[i] == start_words[i]:
            result_mark += 1

    print(f'Your mark: {result_mark}/{amount_words}')

# main
result_prog(6)

