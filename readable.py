""" Readable URL generator """

import random


class readable:
    def __init__(self, capitalize=True, wordCount=3, separator=""):
        """
            Initializes the generator.
            parameters:
                capitalize: If set to true, returns string in CamelCase.
                wordCount: The number of words to use in the URL.
                seperator: The word seperator.
        """

        if not 2 <= wordCount <= 10:
            raise ValueError(
                f"wordCount should be between 2 and 10, inclusive. {wordCount} was given."
            )

        self.capitalize = capitalize
        self.wordCount = wordCount
        self.separator = separator
        self.vowels = "aeiou"
        with open("words/adjectives.txt") as file_obj:
            self.adjectives = " ".join(file_obj.readlines()).strip().split()
        with open("words/nouns.txt") as file_obj:
            self.nouns = " ".join(file_obj.readlines()).strip().split()

    def generate(self):
        wordList = []

        wordList.append(random.choice(self.adjectives))
        wordList.append(random.choice(self.nouns))

        if self.wordCount > 5:
            wordList = random.choices(self.adjectives, k=self.wordCount - 2) + wordList
        else:
            if self.wordCount > 2:
                wordList.insert(0, random.choice(self.adjectives))
            if self.wordCount > 3:
                if wordList[0][0] in self.vowels:
                    wordList.insert(0, "an")
                else:
                    wordList.insert(0, random.choice(("a", "the")))
            if self.wordCount > 4:
                wordList.insert(2, "and")
        if self.capitalize:
            wordList = [word.title() for word in wordList]

        return self.separator.join(wordList)

