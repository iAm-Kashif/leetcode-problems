from collections import defaultdict


class TrieNode():
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.isWord = False


class WordDictionary:

    def __init__(self):
        self.wordlist = defaultdict(list)

    def addWord(self, word: str) -> None:
        if word:
            self.wordlist[len(word)].append(word)

    def search(self, word: str) -> bool:
        if not word: return False
        if not "." in word: return word in self.wordlist[len(word)]
        else:
            for wrd in self.wordlist[len(word)]:
                for idx, ch in enumerate(word):
                    if not ch == "." and not ch == word[idx]:
                        break
            else:
                return True
        return False


class WordDictionary1:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """
        node = self.root
        for ch in word:
            node = node.children[ch]
        node.isWord = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """

        def find(word, node):
            if not word: return node.isWord
            if not word[0] == ".":
                if word[0] in node.children: return find(word[1:], node.children[word[0]])
                return False
            else:
                for n in node.children.values():
                    if find(word[1:], n): return True
                return False

        node = self.root
        return find(word, node)


def main():
    word = WordDictionary()


if __name__ == "__main__":
    main()
