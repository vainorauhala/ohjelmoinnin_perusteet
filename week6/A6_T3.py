

def main():
    print("Program starting.")
    print("This program can copy a file.")
    srcfile = input("Inser filename: ")
    dstfile = input("insert destination filename: ")
    file1 = open(srcfile , "r")
    file2 = open(dstfile, "w")

    for line in file1:
            file2.write(line)

    file1.close()
    file2.close()
    print("File content ready in memory.")
    print(f"Writing content into file '{dstfile}'.")
    print("printCopying operation complete.")
    print("Program ending.")

if __name__ == "__main__":
    main()

