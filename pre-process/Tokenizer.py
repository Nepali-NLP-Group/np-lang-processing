# coding: utf-8
import re


class Tokenizer:
    """Base class for all tokenizers
    """

    def __init__(self):
        # We need this for the build_repr to work properly in py2.7
        pass

    def sentence_tokenize(self, text):
        """
        :param text: text to split into sentences
        :return: a tokenized sentences from the text
        """

        return re.split('(?<=[।?!]) +', text)

    def word_tokenize(self, text):
        """Tokenizes text into words
        Parameter
        --------
        text: text to split into words

        Returns
        -------
        words: non-ascii array of words
        """
        colon_lexicon = ['मूलत:', 'प्रथमत:', 'क्रमश:']

        # Handling punctuations: , " ' ) ( { } [ ] ! ‘ ’ “ ” :- ? । / —
        text = re.sub('\,|\"|\'| \)|\(|\)| \{| \}| \[| \]|!|‘|’|“|”| \:-|\?|।|/|\—', ' ', text)
        words_original = text.split()

        words = []
        for word in words_original:
            if word[len(word) - 1:] == '-':
                if not word == '-':
                    words.append(word[:len(word) - 1])
            else:
                if word[len(word) - 1:] == ':' and word not in colon_lexicon:
                    words.append(word[:len(word) - 1])
                else:
                    words.append(word)

        return words