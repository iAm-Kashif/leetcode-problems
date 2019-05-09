"""
127. Word Ladder
https://leetcode.com/problems/word-ladder/

_author:            Kashif Memon
_python_version:    3.7.2
"""


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: 'List[str]') -> int:

        if endWord not in wordList or not beginWord or not endWord or not wordList: return 0

        L = len(beginWord)

        # Preprocess the wordList into Dictionary with all possible combinations
        import collections
        wordDict = collections.defaultdict(list)

        for word in wordList:
            for idx in range(L):
                wordDict[word[:idx] + "*" + word[idx + 1:]].append(word)

        # {'*ot': ['hot', 'dot', 'lot'], 'h*t': ['hot'], 'ho*': ['hot'],
        # wordLadder Traverse using Queue (BFS)
        q = [(beginWord, 1)]
        visited = {beginWord: True}

        while q:
            curr_word, level = q.pop(0)

            for idx in range(L):
                intermediate_word = curr_word[:idx] + "*" + curr_word[idx + 1:]

                for word in wordDict[intermediate_word]:
                    if word == endWord:
                        return level + 1
                    if word not in visited:
                        visited[word] = True
                        q.append((word, level + 1))
        return 0


def main():
    print(Solution().ladderLength("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]))


if __name__ == "__main__":
    main()
