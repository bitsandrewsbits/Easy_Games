filename = 'UA_words.txt'
words_list_in_file = []

with open(filename, 'rt') as read_f:
    print('Reading words from file...')
    words_list_in_file = [word[:-1] for word in read_f.readlines()] # list of words without '\n'
    with open(filename, 'at') as write_f:
        tmp_word = ''
        print('Writing words into file...')
        while True:
            tmp_word = input('Enter Ukrainian noun word: ')
            if tmp_word == '0':
                break
            if tmp_word in words_list_in_file:
                print('This word exists in file! Try another.')
            else:
                words_list_in_file.append(tmp_word)
                write_f.write(tmp_word + '\n')
