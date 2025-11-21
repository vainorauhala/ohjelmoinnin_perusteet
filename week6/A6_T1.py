

def readfile(fname):
    filehandler = open(fname, "r")
    content = ""
    row = filehandler.readline()
    while row != "":
        content = content + row 
        print(f"MIKÄ ROW ON TÄSSÄKOHTAA: {row}")
        print(f"MIKÄ IHMEEN CONTENT: {content}")
        row = filehandler.readline()
    filehandler.close()
    return content
  



def main() -> None:
    print("Program starting.")
    print("This program can read a file.")
    fname = input("Insert filename: ")
    filecontent = readfile(fname)
    print("#### START {}####" .format(fname))


    print("#### END {}####" .format(fname))
    print("Program ending.")
    return None


if __name__ == "__main__":
    main()
