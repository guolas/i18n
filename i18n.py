"""
Module to provide a function for shortening the words in a sentence, while
keeping the punctuation marks and whitspaces:

    "hello world" -> "h3o w3d"
    "hello, world!" -> "h3o, w3d!"
    "I do it" -> "I-1I d0o i0t"
    "-see,there is that thing" -> "-s1e,t3e i0s t2t t3g"
"""

import re
import unittest

def i18n(sentence):
    """
    Compact the words in a sentence so that they follow the common way of
    shortening words like "internationalization" to "i18n".
    """

    list_of_separators = re.findall(r"\W+", sentence)
    list_of_words = re.findall(r"\w+", sentence)

    list_of_compressed_words = []
    for word in list_of_words:
        # compress the word
        new_word = [word[0], word[-1]]
        new_word.insert(1, str(len(word) - 2))
        list_of_compressed_words.append("".join(new_word))

        new_sentence = []

    if re.match(r"^\W", sentence):
        # My sentence starts with a separator, so add a separator first
        new_sentence.append(list_of_separators.pop(0))

    for word in list_of_compressed_words:
        new_sentence.append(word)
        if len(list_of_separators):
            new_sentence.append(list_of_separators.pop(0))
    return "".join(new_sentence)

class TestI18nMethods(unittest.TestCase):
    """
    Test the method created to compact the words in the i18n notation, if that
    is even a name, but I guess it is clear what that means.
    """

    def test_i18n(self):
        """ Test the shortening with some examples """
        self.assertEqual(i18n("hello world!"), "h3o w3d!")
        self.assertEqual(i18n("hello, world"), "h3o, w3d")
        self.assertEqual(i18n("I do it"), "I-1I d0o i0t")
        self.assertEqual(i18n("see,there is that thing"), "s1e,t3e i0s t2t t3g")
        self.assertEqual(i18n("¿qué hora es?"), "¿q1é h2a e0s?")
        self.assertEqual(i18n("internationalization"), "i18n")

if __name__ == "__main__":
    unittest.main()
