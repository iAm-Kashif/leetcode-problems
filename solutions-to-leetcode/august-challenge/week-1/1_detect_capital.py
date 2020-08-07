class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if word.isupper() or word.islower() or (word[0].isupper() & word[1:].islower()):
            return True
        return False


def main():
    print(Solution().detectCapitalUse("USA"))
    print(Solution().detectCapitalUse("flaG"))


if __name__ == "__main__":
    main()
