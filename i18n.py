import re

def i18n(sentence):
    list_of_separators = re.findall("\W+", sentence)
    list_of_words = re.findall("\w+", sentence)

    list_of_compressed_words = []
    for word in list_of_words:
        # compress the word
        new_word = [word[0], word[-1]]
        new_word.insert(1, str(len(word) - 2))
        list_of_compressed_words.append("".join(new_word))

        new_sentence = []

    if re.match("^\W", sentence):
        # My sentence starts with a separator, so add a separator first
        new_sentence.append(list_of_separators.pop(0))

    for word in list_of_compressed_words:
        new_sentence.append(word)
        if len(list_of_separators):
            new_sentence.append(list_of_separators.pop(0))
    return "".join(new_sentence)

print(i18n("hello world!"))
print(i18n("hello, world"))
print(i18n("I do it"))
print(i18n("see,there is that thing"))
print(i18n("¿qué hora es?"))
