def read_names(filename):
    names = []
    try:
        with open(filename, "r") as f:
            for line in f:
                cleaned = line.strip()
                if cleaned == "":
                    continue
                
                parts = cleaned.split(";")
                for name in parts:
                    name = name.strip()
                    if name != "":
                        names.append(name)
    except FileNotFoundError:
        print(f'File "{filename}" not found.')
        return []
    return names


def analyse(names):
    if len(names) == 0:
        return 0, 0, 0, 0.0

    lengths = [len(n) for n in names]

    count = len(lengths)
    shortest = min(lengths)
    longest = max(lengths)
    average = sum(lengths) / count

    return count, shortest, longest, average


def build_report(count, shortest, longest, average):
    report = "#### REPORT BEGIN ####\n"
    report += f"Name count - {count}\n"
    report += f"Shortest name - {shortest} chars\n"
    report += f"Longest name - {longest} chars\n"
    report += "Average name - {:.2f} chars\n".format(average)
    report += "#### REPORT END ####"
    return report


def main():
    print("Program starting.")
    print("This program analyses a list of names from a file.")

    filename = input("Insert filename to read: ")

    print(f'Reading names from "{filename}".')
    names = read_names(filename)

    print("Analysing names...")
    count, shortest, longest, average = analyse(names)
    print("Analysis complete!")

    report = build_report(count, shortest, longest, average)
    print(report)

    print("Program ending.")


if __name__ == "__main__":
    main()