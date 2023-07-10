def main():
    word = input('word: ')
    print(shorten(word)).lower()


def shorten(word):
    new_word = ""
    for i in range(len(word)):
        if word[i] not in ["a", "e", "i", "o", "u"]:
            new_word += word[i]
    return new_word


if __name__ == "__main__":
    main()