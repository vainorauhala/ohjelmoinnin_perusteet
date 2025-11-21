LOWER_ALPHABETS = "abcdefghijklmnopqrstuvwxyz"
UPPER_ALPHABETS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def shiftCharacter(ch: str, alphabet: str) -> str:
    idx = -1
    i = 0
    while i < len(alphabet):
        if alphabet[i] == ch:
            idx = i
            break
        i += 1
    if idx == -1:
        return ch
    new_idx = (idx + 13) % 26
    return alphabet[new_idx]

def rot13(text: str) -> str:
    result = ""
    for ch in text:
        if ch in LOWER_ALPHABETS:
            result += shiftCharacter(ch, LOWER_ALPHABETS)
        elif ch in UPPER_ALPHABETS:
            result += shiftCharacter(ch, UPPER_ALPHABETS)
        else:
            result += ch
    return result

def writeFile(filename: str, content: str) -> None:
    with open(filename, 'w', encoding="UTF-8") as f:
        f.write(content)
    return None

if __name__ == "__main__":
    pass