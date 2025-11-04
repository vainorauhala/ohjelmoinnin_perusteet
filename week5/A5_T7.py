DELIMITER = ','

def collectWords() -> str:    
    words = ""
    while True:
        w = input("Insert word (empty stops): ")
        if w == "":
            break
        if words != "":
            words += DELIMITER
        words += w
    return words

def analyseWords(PWords: str) -> None:
    if PWords == "":
        word_list = []
    else:
        word_list = PWords.split(DELIMITER)

    word_count = len(word_list)
    char_count = sum(len(w) for w in word_list)
    avg = (char_count / word_count) if word_count > 0 else 0.0

    print(f"- {word_count} Words")
    print(f"- {char_count} Characters")
    print("- {:.2f} Average word length".format(avg))
    return None

def main():
    print("Program starting.")
    words = collectWords()
    analyseWords(words)
    print("Program ending.")
    return None

if __name__ == "__main__":
    main()