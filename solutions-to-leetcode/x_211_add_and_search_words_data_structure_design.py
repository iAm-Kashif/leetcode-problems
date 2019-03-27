import collections

class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.word_dict = collections.defaultdict(set)

    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """
        self.word_dict[len(word)].add(word)

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """
        if not word:
            return False
        if not "." in word:
            return word in self.word_dict