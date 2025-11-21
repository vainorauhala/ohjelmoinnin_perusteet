SEPARATOR = ";"


def readValues(filename: str) -> str:
    file = open(filename, "r", encoding="utf-8")
    text = ""
    first = True

    for line in file:
        line = line.strip()
        if line != "":
            if not first:
                text = text + SEPARATOR
            text = text + line
            first = False

    file.close()
    return text


def analyseValues(values: str) -> str:
    if values == "":
        return "Count;Sum;Greatest;Average\n0;0;0;0.00\n"

    total = 0
    count = 0
    greatest = 0
    current = ""

    values = values + SEPARATOR

    for ch in values:
        if ch != SEPARATOR:
            current = current + ch
        else:
            n = int(current)
            total = total + n
            count = count + 1
            if n > greatest:
                greatest = n
            current = ""

    average = total / count

    return "Count;Sum;Greatest;Average\n" + \
           str(count) + ";" + \
           str(total) + ";" + \
           str(greatest) + ";" + \
           f"{average:.2f}\n"


def main():
    print("Program starting.")
    filename = input("Insert filename: ")

    values = readValues(filename)
    result = analyseValues(values)

    print("#### Number analysis - START ####")
    print(f'File "{filename}" results:')
    print(result)
    print("#### Number analysis - END ####")
    print("Program ending.")


if __name__ == "__main__":
    main()