import re

# generate random word list

text = None
try:
    f = open("De finibus bonorum et malorum.txt", "r")
    text = f.read()
    f.close()
except IOError:
    pass

if (text):
    words = []
    results = re.findall(r"[a-zA-Z]+", text)
    for word in results:
        word = word.lower()
        if word not in words:
            words.append(word)

    words.sort()

    try:
        wordList = open("word_list_random.txt", "w")
        for w in words:
            wordList.write("%s\n" % w)
        wordList.close()
    except IOError:
        pass


# generate fixed word list

text = None
try:
    f = open("Lorem Ipsum Fixed Text.txt", "r")
    text = f.read()
    f.close()
except IOError:
    pass

if (text):
    results = re.findall(r"[a-zA-Z]+|,|\.", text)

    try:
        wordList = open("word_list_fixed.txt", "w")
        for w in results:
            wordList.write("%s\n" % w)
        wordList.close()
    except IOError:
        pass
