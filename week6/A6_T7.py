import os

PLAYER_PROGRESS_FILE = "player_progress.txt"

PLACES = {
    0: "home",
    1: "Galba's palace",
    2: "Otho's palace",
    3: "Vitellius' palace",
    4: "Vespasian's palace"
}


def rot13(text: str) -> str:
    result_chars = []
    for ch in text:
        if "a" <= ch <= "z":
           
            offset = ord("a")
            result_chars.append(chr((ord(ch) - offset + 13) % 26 + offset))
        elif "A" <= ch <= "Z":
           
            offset = ord("A")
            result_chars.append(chr((ord(ch) - offset + 13) % 26 + offset))
        else:
           
            result_chars.append(ch)
    return "".join(result_chars)


def ensure_progress_file_exists() -> None:
    """Create player_progress.txt with initial data if it does not exist."""
    if not os.path.exists(PLAYER_PROGRESS_FILE):
        with open(PLAYER_PROGRESS_FILE, "w", encoding="utf-8") as f:
            f.write("current_location;next_location;passphrase\n")
          
            f.write("0;1;qvfpvcyvar\n")


def read_travel_progress() -> tuple[int, int, str]:
    with open(PLAYER_PROGRESS_FILE, "r", encoding="utf-8") as f:
        lines = f.read().splitlines()

    if len(lines) < 2:
        raise ValueError("player_progress.txt is missing the data row.")

    header = lines[0] 
    data_row = lines[1]

    parts = data_row.split(";")
    if len(parts) != 3:
        raise ValueError("Data row in player_progress.txt is malformed.")

    current_location = int(parts[0])
    next_location = int(parts[1])
    passphrase_cipher = parts[2]

    return current_location, next_location, passphrase_cipher


def append_cipher_line_to_progress(cipher_line: str) -> None:
    with open(PLAYER_PROGRESS_FILE, "a", encoding="utf-8") as f:
        f.write(cipher_line + "\n")


def save_plain_message(next_location: int, plain_passphrase: str, plain_message: str) -> None:

    filename = f"{next_location}-{plain_passphrase}.txt"
    with open(filename, "w", encoding="utf-8") as f:
        f.write(plain_message)


def main() -> None:
 
    ensure_progress_file_exists()

 
    current_location, next_location, passphrase_cipher = read_travel_progress()

 
    passphrase_plain = rot13(passphrase_cipher)

   
    message_filename = f"{next_location}_{passphrase_cipher}.gkg"

  
    print("Travel starting.")
    print(f"Currently at {PLACES.get(current_location, 'unknown location')}.")

    print(f"Travelling to {PLACES.get(next_location, 'unknown destination')}...")
    print(f"...Arriving to the {PLACES.get(next_location, 'unknown destination')}.")

    print("Passing the guard at the entrance.")
    print(f"\"{passphrase_plain.capitalize()}!\"")

    print("Looking for the message in the palace...")

    if not os.path.exists(message_filename):
     
        print(f"Error: Cannot find the message file '{message_filename}'.")
        print("Travel ending.")
        return

 
    with open(message_filename, "r", encoding="utf-8") as f:
        cipher_lines = f.read().splitlines()

    if not cipher_lines:
        print("Error: The message file is empty.")
        print("Travel ending.")
        return

    print("Ah, there it is! Seems cryptic.")


    first_cipher_line = cipher_lines[0]
    append_cipher_line_to_progress(first_cipher_line)

    print("[Game] Progress autosaved!")

   
    print("Deciphering Emperor's message...")
    cipher_full_text = "\n".join(cipher_lines)
    plain_full_text = rot13(cipher_full_text)

    save_plain_message(next_location, passphrase_plain, plain_full_text)
    print("Looks like I've got now the plain version copy of the Emperor's message.")
    print("Time to leave...")
    print("Travel ending.")


if __name__ == "__main__":
    main()