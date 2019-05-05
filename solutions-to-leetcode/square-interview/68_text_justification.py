"""
68. Text Justification
https://leetcode.com/problems/text-justification/

_author:            Kashif Memon
_python_version:    3.7.2
"""


class Solution:
    def fullJustify(self, words: 'List[str]', maxWidth: int) -> 'List[str]':
        idx = 0  # number of words to keep track
        out = []  # final output

        def getWords():  # gets the number of words that can fit in one line
            numWords = 0  # number of words that can fit in one line.
            line = ""

            while len(line) <= maxWidth and idx + numWords <= len(words):
                numWords += 1
                line = " ".join(words[idx:idx + numWords])
            return numWords - 1  # as index of words starts with 0.

        def addSpaces(wordsInLine):  # once the number of words are identified, time to form the line by adding spaces
            line = " ".join(words[idx:idx + wordsInLine])

            if wordsInLine == 1 or idx + wordsInLine == len(words):  # only 1 word or no more words left(aka last line)
                # we need to left justify the line
                spaces = maxWidth - len(line)
                line = line + " " * spaces
            else:
                spaces = maxWidth - len(line) + (wordsInLine - 1)  # total number of spaces
                # avg space per word, k-1 as we only need space "between" words.
                space = spaces // (wordsInLine - 1)
                # number of left words -> words that have 1 more space than other words on the right
                left = spaces % (wordsInLine - 1)

                if left > 0:
                    line = (" " * (space + 1)).join(words[idx:idx + left])  # left words
                    line += " " * (space + 1)  # spaces between left words & right words
                    line += (" " * space).join(words[idx + left:idx + wordsInLine])  # right words
                else:
                    line = (" " * space).join(words[idx:idx + wordsInLine])

            return line

        while idx < len(words):
            wordsInLine = getWords()
            line = addSpaces(wordsInLine)
            out.append(line)
            idx += wordsInLine
        return out


def main():
    print(Solution().fullJustify(["This", "is", "an", "example", "of", "text", "justification."], 16))


if __name__ == "__main__":
    main()
